from inverted_index import InvertedIndex
import os
#just test commit

def main():
    os.chdir('./std_docs_txt')
    docs = os.listdir(os.getcwd())
    index = InvertedIndex(docs)
    index.build()

    print(index.description_index)


if __name__ == '__main__':
    main()
