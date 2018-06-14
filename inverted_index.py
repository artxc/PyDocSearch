from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer


class InvertedIndex:

    def __init__(self, corpus):
        self.corpus = corpus
        self.description_index = defaultdict(set)

    def read_file(self, file):
        with open(file) as f:
            words = word_tokenize(f.read())
            buf = []
            for word in words:
                split_word = word.split('.')
                if len(split_word) > 1:
                    buf.extend(split_word)
            words.extend(buf)
        return words

    def build(self):
        stemmer = PorterStemmer()
        stop_words = set(stopwords.words('english'))

        for i, file in enumerate(self.corpus):
            words = self.read_file(file)
            for word in words:
                if word not in stop_words:
                    stemmed_word = stemmer.stem(word)
                    self.description_index[stemmed_word].add(i)

    def get_postings(self, word):
        return self.description_index[word]
