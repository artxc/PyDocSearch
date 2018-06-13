from inverted_index import InvertedIndex
import os


def main():
    docs = os.listdir()
    index = InvertedIndex(docs)
    index.build()
    # Process queries


if __name__ == '__main__':
    main()
