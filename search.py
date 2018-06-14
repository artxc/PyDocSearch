import os
from inverted_index import InvertedIndex
from query_handler import QueryHandler

RELATIVE_PATH_TO_CORPUS = './std_docs'


def main():
    os.chdir(RELATIVE_PATH_TO_CORPUS)

    docs = os.listdir(os.getcwd())
    index = InvertedIndex(docs)
    index.build()

    QueryHandler(index).loop()


if __name__ == '__main__':
    main()
