from inverted_index import InvertedIndex
import os


def main():
    os.chdir('./std_docs_txt')
    docs = os.listdir(os.getcwd())
    index = InvertedIndex(docs)
    index.build()


if __name__ == '__main__':
    main()
