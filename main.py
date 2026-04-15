from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Обучающий курс: \"Переработка нефти\"")
        self.setWindowIcon(QIcon(QPixmap("images/icon.png")))
        self.showNormal()

app = QApplication()
window = MainWindow()
window.show()
app.exec()