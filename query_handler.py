from nltk.stem.porter import PorterStemmer


class QueryHandler:

    def __init__(self, index):
        self.index = index
        self.stemmer = PorterStemmer()

    def proccess_query(self, query):
        terms = [self.stemmer.stem(token) for token in query.split()]
        doc_ids = set.intersection(*[self.index.get_postings(term) for term in terms])

        print('Найденные документы:')
        for i in doc_ids:
            print(self.index.corpus[i])

    def loop(self):
        print('Введите запросы после приглашения. Наберите -exit, чтобы выйти')

        while True:
            query = input('> ').strip()
            if query == '-exit':
                break

            self.proccess_query(query)
            print()
