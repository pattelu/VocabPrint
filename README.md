VocabPrint is a simple application for converting CSV files into clean, printable PDF tables - without the hassle of using spreadsheet applications.

![menu gui](https://github.com/pattelu/VocabPrint/blob/main/img/gui.png?raw=true)

# How it works?
You need a CSV file with following columns:
KANJI | HIRAGANA | TRANSLATION | SENTENCE | SENTENCE TRANSLATION

The PDF file is designed for printing:
- Front:
  - ID | KANJI | HIRAGANA | TRANSLATION | SENTENCE
- Back:
  - ID | SENTENCE TRANSLATION

This allows you to have all the necessary information on the front page while still being able to check the sentence translation on the back when needed.

By default, the PDF is configured to be printed in landscape mode with short-edge flipping.

See [example](https://github.com/pattelu/VocabPrint/tree/main/example) folder.

# Why I created that?
- I spent too much time fighting with spreadsheet applications just to get the print result I wanted.
- Learning from a digital version can be distracting, and sometimes you want to study in a more comfortable place and position.
- Sometimes it's better to have a few sheets of paper to review than to carry your entire PC with you. Additionally, when you use paper instead of your phone, you look smarter. 😎

# What I used on this project:
- [Pandas](https://pandas.pydata.org/) for reading CSV file.
- [ReportLab](https://www.reportlab.com/) for generating PDFs with tables.
- [pypdf](https://pypdf.readthedocs.io/en/stable/) for combining PDF files in the correct order.
- [PySide6](https://doc.qt.io/qtforpython-6/index.html) for creating the GUI.
- [PyInstaller](https://pyinstaller.org/) for packaging the application as an executable file.
