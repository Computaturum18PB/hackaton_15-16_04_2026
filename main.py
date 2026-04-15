from PySide6.QtWidgets import (QApplication, QMainWindow)
# from PySide6.QtCore import Qt, Slot
# from PySide6.QtGui import QFont
from MainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
