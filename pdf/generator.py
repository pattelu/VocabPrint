from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    PageBreak,
    TableStyle,
    Paragraph,
)


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
        rightMargin=1,
        leftMargin=1,
        topMargin=1,
        bottomMargin=1,
    )

    elements = []

    for chunk in chunks:
        front = chunk.iloc[:, 0:5]
        back = chunk.iloc[:, 5:7]

        front_table = Table(front.values.tolist())
        front_table.hAlign = "LEFT"
        for row in range(0, len(chunk)):
            if row % 2 == 0:
                front_table.setStyle(
                    TableStyle(
                        [
                            ("FONT", (0, 0), (0, -1), "NotoSans"),
                            ("FONT", (1, 0), (1, -1), "NotoSansCJK"),
                            ("FONT", (2, 0), (2, -1), "NotoSansCJK"),
                            ("FONT", (3, 0), (3, -1), "NotoSans"),
                            ("FONT", (4, 0), (4, -1), "NotoSansCJK"),
                            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                            ("BACKGROUND", (0, row), (-1, row), colors.lightgrey),
                        ]
                    )
                )
            else:
                front_table.setStyle(
                    TableStyle(
                        [
                            ("FONT", (0, 0), (0, -1), "NotoSans"),
                            ("FONT", (1, 0), (1, -1), "NotoSansCJK"),
                            ("FONT", (2, 0), (2, -1), "NotoSansCJK"),
                            ("FONT", (3, 0), (3, -1), "NotoSans"),
                            ("FONT", (4, 0), (4, -1), "NotoSansCJK"),
                            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                        ]
                    )
                )
        back_table = Table(back.values.tolist())
        back_table.hAlign = "LEFT"
        for row in range(0, len(chunk)):
            if row % 2 == 0:
                back_table.setStyle(
                    TableStyle(
                        [
                            ("FONT", (5, 0), (5, -1), "NotoSans"),
                            ("FONT", (6, 0), (6, -1), "NotoSans"),
                            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                            ("BACKGROUND", (0, row), (-1, row), colors.lightgrey),
                        ]
                    )
                )
            else:
                back_table.setStyle(
                    TableStyle(
                        [
                            ("FONT", (5, 0), (5, -1), "NotoSans"),
                            ("FONT", (6, 0), (6, -1), "NotoSans"),
                            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                        ]
                    )
                )

        elements.append(front_table)
        elements.append(PageBreak())
        elements.append(back_table)
        elements.append(PageBreak())

    pdf.build(elements)
