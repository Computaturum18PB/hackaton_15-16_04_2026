from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QMainWindow, QWidget
from PySide6.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Обучающий курс: \"Переработка нефти\"")
        self.setWindowIcon(QIcon(QPixmap("images/icon.png")))
        self.showMaximized()
        
        widget = QWidget()
        self.setCentralWidget(widget)
        
        self.main_label = QLabel("Добро пожаловать на обучающий курс: Переработка нефти!")
        
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.main_label)
        
        

app = QApplication()
window = MainWindow()
window.show()
app.exec()