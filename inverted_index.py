from collections import defaultdict


class InvertedIndex:

    def __init__(self, corpus):
        self.corpus = corpus
        self.index = defaultdict(list)

    def build(self):
        pass
