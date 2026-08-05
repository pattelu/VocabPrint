import re
from io import BytesIO

from pypdf import PdfWriter, PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    PageBreak,
    TableStyle,
    Paragraph,
)

from reportlab.pdfbase.pdfmetrics import stringWidth


def create_pdf(vocabs):
    pdfmetrics.registerFont(TTFont("NotoSans", "fonts/NotoSans-Regular.ttf"))
    pdfmetrics.registerFont(
        TTFont("JapaneseFont", "fonts/NotoSansCJKjp-Regular.ttf", subfontIndex=0)
    )

    buffer1 = BytesIO()
    buffer2 = BytesIO()

    pdf = SimpleDocTemplate(
        buffer1,
        pagesize=landscape(A4),
        rightMargin=10,
        leftMargin=10,
        topMargin=10,
        bottomMargin=10,
    )

    pdf2 = SimpleDocTemplate(
        buffer2,
        pagesize=landscape(A4),
        rightMargin=10,
        leftMargin=10,
        topMargin=10,
        bottomMargin=10,
    )

    jp_style = ParagraphStyle(
        "JPSentence",
        fontName="JapaneseFont",
        wordWrap="CJK",
        fontSize=10,
        leading=14,
    )

    latin_style = ParagraphStyle(
        "LatinSentence",
        fontName="JapaneseFont",
        fontSize=10,
        leading=14,
    )

    style_front = TableStyle(
        [
            ("FONT", (0, 0), (0, -1), "NotoSans"),
            ("FONT", (1, 0), (1, -1), "JapaneseFont"),
            ("FONT", (2, 0), (2, -1), "JapaneseFont"),
            ("FONT", (3, 0), (3, -1), "NotoSans"),
            # ("FONT", (4, 0), (4, -1), "JapaneseFont"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ]
    )

    style_back = TableStyle(
        [
            ("FONT", (5, 0), (5, -1), "NotoSans"),
            # ("FONT", (6, 0), (6, -1), "NotoSans"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ]
    )

    front = vocabs.iloc[:, 0:5]
    back = vocabs.iloc[:, 5:7]

    tmp_front_table = front.values.tolist()
    tmp_back_table = back.values.tolist()

    for row in range(0, len(vocabs)):
        if row % 2 == 0:
            style_front.add("BACKGROUND", (0, row), (-1, row), colors.lightgrey)
            style_back.add("BACKGROUND", (0, row), (-1, row), colors.lightgrey)

    front_table = []
    back_table = []

    for row in tmp_front_table:
        row[-1] = Paragraph(str(row[-1]), jp_style)
        front_table.append(row)

    for row in tmp_back_table:
        row[-1] = Paragraph(str(row[-1]), latin_style)
        back_table.append(row)

    available_width = pdf.width

    front_width = get_all_width(front_table)
    front_width.append(available_width - sum(front_width) - 10)
    front_table = Table(front_table, colWidths=front_width)

    front_table.wrap(0, 0)
    row_height = front_table._rowHeights

    back_width = get_all_width(back_table)
    back_width.append(available_width - sum(back_width) - 10)
    back_table = Table(back_table, colWidths=back_width, rowHeights=row_height)

    front_table.setStyle(style_front)
    back_table.setStyle(style_back)

    elements_front = []
    elements_back = []

    elements_front.append(front_table)
    elements_front.append(PageBreak())

    elements_back.append(back_table)
    elements_back.append(PageBreak())

    pdf.build(elements_front)
    buffer1 = buffer1.getvalue()

    pdf2.build(elements_back)
    buffer2 = buffer2.getvalue()

    return buffer1, buffer2


def merge_pdf(save_path, filename, buffers):
    front = PdfReader(BytesIO(buffers[0]))
    back = PdfReader(BytesIO(buffers[1]))

    merger = PdfWriter()

    pages = len(front.pages)

    for i in range(pages):
        merger.add_page(front.pages[i])
        merger.add_page(back.pages[i])

    with open(save_path + filename, "wb") as file:
        merger.write(file)


def get_column_width(rows, column, font_name, font_size, padding=10):
    max_width = 0

    for row in rows:
        text = str(row[column])

        width = stringWidth(text, font_name, font_size)

        max_width = max(max_width, width)

    return max_width + padding


def get_all_width(rows):
    results = []

    if not rows:
        return results

    columns = len(rows[0])

    for column in range(columns):
        if column == columns - 1:
            break

        font_name = "NotoSans"

        for row in rows:
            if is_japanese_text(str(row[column])):
                font_name = "JapaneseFont"
                break

        width = get_column_width(rows, column, font_name, 10)

        results.append(width)

    return results


def is_japanese_text(text):
    if not isinstance(text, str):
        return False

    return bool(re.search(r"[\u3040-\u30ff\u3400-\u9fff\uf900-\ufaff]", text))
