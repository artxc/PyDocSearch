from nltk.stem.porter import PorterStemmer
from collections import defaultdict


class QueryHandler:

    def __init__(self, index, class_score=8, attribut_score=5, description_score=3):
        self.index = index
        self.stemmer = PorterStemmer()
        self.class_score = class_score
        self.attribut_score = attribut_score
        self.description_score = description_score

    def count_term_score(self, doc_scores, term):
        for doc_id in self.index.get_class_postings(term):
            doc_scores[doc_id] += self.class_score
        for doc_id in self.index.get_attribut_postings(term):
            doc_scores[doc_id] += self.attribut_score
        for doc_id in self.index.get_description_postings(self.stemmer.stem(term)):
            doc_scores[doc_id] += self.description_score

    def process_query(self, query):
        doc_scores = defaultdict(int)
        terms = query.split()

        for term in terms:
            if '.' in term:
                for subterm in term.split('.'):
                    self.count_term_score(doc_scores, subterm)
            else:
                self.count_term_score(doc_scores, term)

        doc_ids = [doc_id for doc_id in sorted(doc_scores, key=doc_scores.get, reverse=True)]

        if doc_ids:
            print('Найденные документы:')
            for i in doc_ids:
                print(self.index.corpus[i])
        else:
            print('Ничего не найдено.')

    def loop(self):
        print('Введите запросы после приглашения. Наберите -exit, чтобы выйти')

        while True:
            query = input('> ').strip()
            if query == '-exit':
                break

            self.process_query(query)
            print()
    