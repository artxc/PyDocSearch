from nltk.stem.porter import PorterStemmer


class QueryHandler:

    def __init__(self, index):
        self.index = index

    def loop(self):
        stemmer = PorterStemmer()
        print('Введите запросы после приглашения. Наберите -exit, чтобы выйти')

        while True:
            query = input('> ').strip()
            if query == '-exit':
                break

            terms = [stemmer.stem(token) for token in query.split()]
            doc_ids = set.intersection(*[self.index.get_postings(term) for term in terms])

            print('Найденные документы:')
            for i in doc_ids:
                print(self.index.corpus[i])
            print()
