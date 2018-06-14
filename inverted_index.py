from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer


class InvertedIndex:

    def __init__(self, corpus):
        self.corpus = corpus
        self.description_index = defaultdict(set)

    def tokenize_file(self, file_name):
        with open(file_name) as f:
            tokens = word_tokenize(f.read())
            dot_tokens = [token.split('.') for token in tokens if '.' in tokens]

            for token in dot_tokens:
                tokens.extend(token)

        return tokens

    def build(self):
        stemmer = PorterStemmer()
        stop_words = set(stopwords.words('english'))

        for i, file_name in enumerate(self.corpus):
            tokens = self.tokenize_file(file_name)
            for token in tokens:
                if token not in stop_words:
                    stemmed_word = stemmer.stem(token)
                    self.description_index[stemmed_word].add(i)

    def get_postings(self, word):
        return self.description_index[word]
