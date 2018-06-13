from nltk.stem.porter import PorterStemmer

class QueryHandler:

    def __init__(self, index):
        self.index = index

    def loop(self):
        enumerate_corpus=dict((i,file) for i,file in enumerate(self.index.get_corpus()))
        stemmer = PorterStemmer()

        while True:
            query=input('Введите запрос\n').split()
            query=list(map(stemmer.stem,query))
            doc_numbers=set.intersection(*[self.index.get_description_index(word) for word in query])
            print('Документы:')
            for i in doc_numbers:
                print(enumerate_corpus[i])


