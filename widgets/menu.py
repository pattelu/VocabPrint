import subprocess
import sys

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QFileDialog

from readers import csv_reader
from pdf import generator
from ui.ui_menu import Ui_Form


class MenuWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tool_csv.clicked.connect(self.set_csv_path)
        self.tool_save.clicked.connect(self.set_save_folder)

        self.btn_generate_pdf.clicked.connect(self.generate_pdf)
        self.btn_open_save_folder.clicked.connect(self.open_save_folder)

    def generate_pdf(self):
        self.label_info.setText("")
        csv_path = self.line_csv_file.text()
        save_path = self.line_save_folder.text()
        filename = self.line_filename.text()
        if not filename.endswith(".pdf"):
            filename = filename + ".pdf"

        vocabs = csv_reader.read_csv(csv_path)
        buffers = generator.create_pdf(vocabs)
        generator.merge_pdf(save_path, filename, buffers)
        self.label_info.setText(f"File generated in: {save_path}")

    def set_csv_path(self):
        csv, ext = QFileDialog.getOpenFileName(
            self, "Select CSV", "", "CSV file (*.csv)"
        )
        self.line_csv_file.setText(str(csv))

    def set_save_folder(self):
        save_dir = QFileDialog.getExistingDirectory()
        self.line_save_folder.setText(f"{save_dir}/")

    def get_save_path(self):
        self.label_info.setText("")

        if self.line_save_folder.text() == "" or self.line_filename.text() == "":
            return None

        save_path = f"{self.line_save_folder.text()}{self.line_filename.text()}"

        if not save_path.endswith(".pdf"):
            save_path = save_path + ".pdf"

        return save_path

    def open_save_folder(self):
        self.label_info.setText("")

        save_path = self.line_save_folder.text()

        if save_path == "":
            self.label_info.setText(f"Wrong path to save directory")
        else:
            try:
                if sys.platform == "win32":
                    subprocess.Popen(["explorer", str(save_path)])
                elif sys.platform == "darwin":  # macOS
                    subprocess.Popen(["open", str(save_path)])
                else:  # Linux
                    subprocess.Popen(["xdg-open", str(save_path)])
            except Exception as e:
                self.label_info.setText(f"Wrong path to save directory. Exception: {e}")
