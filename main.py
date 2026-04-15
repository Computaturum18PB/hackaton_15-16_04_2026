from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QGridLayout, QPushButton)
from PySide6.QtGui import QPixmap

from BaseWindow import BaseWizard1


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        icon = QPixmap("/images/icon.png")

        self.setWindowTitle("Обучающий курс: \"Переработка нефти\"")
        self.setWindowIcon(icon)
        self.setFixedSize(500, 500)

        main_layuot = QVBoxLayout()

        title_label = QLabel("Курс про переработку нефти")
        main_layuot.addWidget(title_label)

        grid_layout = QGridLayout()

        label1 = QLabel("Переработка нефти")
        label2 = QLabel("Первичная переработка нефти")
        label3 = QLabel("Вторичная переработка нефти")

        button1 = QPushButton("Перейти")
        button2 = QPushButton("Перейти")
        button3 = QPushButton("Перейти")

        button1.clicked.connect(self.start_theme_1)

        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(label2, 1, 0)
        grid_layout.addWidget(label3, 2, 0)
        grid_layout.addWidget(button1, 0, 1)
        grid_layout.addWidget(button2, 1, 1)
        grid_layout.addWidget(button3, 2, 1)
        main_layuot.addLayout(grid_layout)

        self.setLayout(main_layuot)

    @Slot()
    def start_theme_1(self):
        list = [0, 0, 0, 1, 1, 1]
        wizard = BaseWizard1(len(list), list, self)
        wizard.show()

app = QApplication()
window = MainWindow()
window.show()
app.exec()
