import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

from src import MainWindow

def main():
    app = QApplication(sys.argv)
    app_icon = QIcon("flacsplitter.png")
    app.setWindowIcon(app_icon)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
