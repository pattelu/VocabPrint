from PySide6.QtWidgets import (
    QApplication,
)
from widgets.menu import MenuWindow


def main():
    app = QApplication([])

    menu_window = MenuWindow()
    menu_window.show()

    app.exec()


if __name__ == "__main__":
    main()
