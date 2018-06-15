from nltk.stem.porter import PorterStemmer
from collections import defaultdict
import webbrowser
import os


class QueryHandler:

    def __init__(self, index):
        self.index = index
        self.stemmer = PorterStemmer()
        self.class_score = 5
        self.attribute_score = 8
        self.description_score = 1
        self.url = os.getcwd() + '/'

    def process_query(self, query):
        tokens = query.lower().split()
        doc_scores = defaultdict(int)

        for token in tokens:
            if '.' in token:
                compound_token = token.split('.')
                for class_name in compound_token[:-1]:
                    for posting in self.index.classes_index[class_name]:
                        doc_scores[posting] += self.class_score

                for posting in self.index.attributes_index[compound_token[-1]]:
                    doc_scores[posting] += self.attribute_score
            else:
                for posting in self.index.classes_index[token]:
                    doc_scores[posting] += self.class_score
                for posting in self.index.attributes_index[token]:
                    doc_scores[posting] += self.attribute_score
                for posting in self.index.description_index[self.stemmer.stem(token)]:
                    doc_scores[posting] += self.description_score

        if doc_scores:
            print('Найденные документы:')
            for doc_id in sorted(doc_scores, key=doc_scores.get, reverse=True):
                print(self.index.corpus[doc_id], f'(score = {doc_scores[doc_id]})')
                
        while True:
            doc_to_open = input('Какой из документов желаете открыть в браузере?\n> ')
            if doc_to_open == 'n':
                break
            for word in tokens:
                word = word.split(".")[-1]
                webbrowser.open_new_tab(self.url + doc_to_open + '#' + doc_to_open[:-5] + '.' + word.strip())
            continue_opening = input('Ещё?(y/n)\n> ')
            if continue_opening == 'n':
                break
        else:
            print('Ничего не найдено')

    def loop(self):
        print('Введите запросы после приглашения. Наберите -exit, чтобы выйти\n')

        while True:
            query = input('Введите новый запрос\n> ').strip()
            if query == '-exit':
                break

            self.process_query(query)
            print()
