from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        icon = QPixmap("/images/icon.png")

        self.setWindowTitle("Обучающий курс: \"Переработка нефти\"")
        self.setWindowIcon(icon)
        self.setFixedSize(500, 500)
        

app = QApplication()
window = MainWindow()
window.show()
app.exec()
