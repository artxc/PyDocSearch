from bs4 import BeautifulSoup
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer


class InvertedIndex:

    def __init__(self, corpus):
        self.corpus = corpus
        self.classes_index = defaultdict(set)
        self.attributes_index = defaultdict(set)
        self.description_index = defaultdict(set)

    def build_attributes_index(self, doc_id, soup):
        attribute_names = [attr.get_text() for attr in soup.find_all('code', {'class': 'descname'})]

        for attr in attribute_names:
            self.attributes_index.add(doc_id)

    def build_classes_index(self, doc_id, soup):
        class_hierarchies = [_class.get_text() for _class in soup.find_all('code', {'class': 'descclassname'})]

        for _class in class_hierarchies:
            class_names = _class[:-1].split('.')  # _class[:-1] to get rid of trailing dot
            for class_name in class_names:
                self.classes_index[class_name].add(doc_id)

    def build_description_index(self, doc_id, soup):
        stemmer = PorterStemmer()
        stop_words = set(stopwords.words('english'))

        descriptions = [desc.get_text() for desc in soup.find_all('p')]
        for description in descriptions:
            tokens = map(str.lower, word_tokenize(description))
            terms = [stemmer.stem(token) for token in tokens if token not in stop_words]
            for term in terms:
                self.description_index[term].add(doc_id)

    def build(self):
        for doc_id, file_name in enumerate(self.corpus):
            with open(file_name) as f:
                soup = BeautifulSoup(f, 'lxml')

            self.build_attributes_index(doc_id, soup)
            self.build_classes_index(doc_id, soup)
            self.build_description_index(doc_id, soup)
