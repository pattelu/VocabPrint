# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.setWindowModality(Qt.WindowModality.NonModal)
        Form.resize(503, 247)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(750, 290))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.line_csv_file = QLineEdit(Form)
        self.line_csv_file.setObjectName("line_csv_file")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.line_csv_file.sizePolicy().hasHeightForWidth()
        )
        self.line_csv_file.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.line_csv_file)

        self.tool_csv = QToolButton(Form)
        self.tool_csv.setObjectName("tool_csv")

        self.horizontalLayout.addWidget(self.tool_csv)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.line_save_folder = QLineEdit(Form)
        self.line_save_folder.setObjectName("line_save_folder")
        sizePolicy1.setHeightForWidth(
            self.line_save_folder.sizePolicy().hasHeightForWidth()
        )
        self.line_save_folder.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.line_save_folder)

        self.tool_save = QToolButton(Form)
        self.tool_save.setObjectName("tool_save")

        self.horizontalLayout_3.addWidget(self.tool_save)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.line_filename = QLineEdit(Form)
        self.line_filename.setObjectName("line_filename")
        sizePolicy1.setHeightForWidth(
            self.line_filename.sizePolicy().hasHeightForWidth()
        )
        self.line_filename.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.line_filename)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line = QFrame(Form)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_info = QLabel(Form)
        self.label_info.setObjectName("label_info")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy2)
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_info)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_generate_pdf = QPushButton(Form)
        self.btn_generate_pdf.setObjectName("btn_generate_pdf")

        self.verticalLayout_3.addWidget(self.btn_generate_pdf)

        self.btn_open_save_folder = QPushButton(Form)
        self.btn_open_save_folder.setObjectName("btn_open_save_folder")

        self.verticalLayout_3.addWidget(self.btn_open_save_folder)

        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "VocabPrint", None))
        self.label.setText(QCoreApplication.translate("Form", "Select .csv file", None))
        self.tool_csv.setText(QCoreApplication.translate("Form", "...", None))
        self.label_5.setText(
            QCoreApplication.translate("Form", "Select save folder", None)
        )
        self.tool_save.setText(QCoreApplication.translate("Form", "...", None))
        self.label_6.setText(QCoreApplication.translate("Form", "PDF file name", None))
        self.line_filename.setText(
            QCoreApplication.translate("Form", "vocabs.pdf", None)
        )
        self.label_info.setText("")
        self.btn_generate_pdf.setText(
            QCoreApplication.translate("Form", "Generate PDF", None)
        )
        self.btn_open_save_folder.setText(
            QCoreApplication.translate("Form", "Open save folder", None)
        )

    # retranslateUi
