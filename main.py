from readers import csv_reader
from pdf import generator


def main():
    vocabs = csv_reader.read_csv("vocab.csv")
    generator.create_pdf(vocabs)
    generator.merge_pdf()


if __name__ == "__main__":
    main()
