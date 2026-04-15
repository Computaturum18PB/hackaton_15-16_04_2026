from PySide6.QtWidgets import (QMainWindow)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Обучающий курс: переработка нефти")
        self.setIcon("image/icon.png")


