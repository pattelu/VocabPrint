from readers import csv_reader
from pdf import generator


def main():
    vocabs = csv_reader.read_csv("vocab.csv")
    chunks = generator.create_chunks(vocabs)
    generator.create_pdf(chunks)


if __name__ == "__main__":
    main()
