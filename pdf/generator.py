import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
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


def create_chunks(df):
    rows_per_page = 32

    chunks = []

    for start in range(0, len(df), rows_per_page):
        end = start + rows_per_page

        chunks.append(df.iloc[start:end])

    return chunks


def create_pdf(chunks):
    pdfmetrics.registerFont(TTFont("NotoSans", "fonts/NotoSans-Regular.ttf"))
    pdfmetrics.registerFont(
        TTFont("NotoSansCJK", "fonts/NotoSansCJKjp-Regular.ttf", subfontIndex=0)
    )

    pdf = SimpleDocTemplate(
        "vocabs.pdf",
        pagesize=landscape(A4),
        rightMargin=10,
        leftMargin=10,
        topMargin=10,
        bottomMargin=10,
    )

    jp_style = ParagraphStyle(
        "JPSentence",
        fontName="NotoSansCJK",
        wordWrap="CJK",
        fontSize=10,
        leading=14,
    )

    latin_style = ParagraphStyle(
        "LatinSentence",
        fontName="NotoSans",
        wordWrap="CJK",
        fontSize=10,
        leading=14,
    )

    style_front = TableStyle(
        [
            ("FONT", (0, 0), (0, -1), "NotoSans"),
            ("FONT", (1, 0), (1, -1), "NotoSansCJK"),
            ("FONT", (2, 0), (2, -1), "NotoSansCJK"),
            ("FONT", (3, 0), (3, -1), "NotoSans"),
            # ("FONT", (4, 0), (4, -1), "NotoSansCJK"),
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

    elements = []

    for chunk in chunks:
        front = chunk.iloc[:, 0:5]
        back = chunk.iloc[:, 5:7]

        tmp_front_table = front.values.tolist()
        tmp_back_table = back.values.tolist()

        for row in range(0, len(chunk)):
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

        back_width = get_all_width(back_table)
        back_width.append(available_width - sum(back_width) - 10)
        back_table = Table(back_table, colWidths=back_width)

        front_table.setStyle(style_front)
        back_table.setStyle(style_back)

        elements.append(front_table)
        elements.append(PageBreak())
        elements.append(back_table)
        elements.append(PageBreak())

    pdf.build(elements)


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
                font_name = "NotoSansCJK"
                break

        width = get_column_width(rows, column, font_name, 10)

        results.append(width)

    return results


def is_japanese_text(text):
    if not isinstance(text, str):
        return False

    return bool(re.search(r"[\u3040-\u30ff\u3400-\u9fff\uf900-\ufaff]", text))
