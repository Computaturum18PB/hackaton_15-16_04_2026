from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QWizardPage,
                               QGroupBox, QPushButton, QLabel, QLineEdit)

class Shablon(QWizardPage):
    def __init__(self, count, number, type):
        super().__init__()
        self.count = count
        self.number = number

        if(type == 0):
            main_layout = QVBoxLayout()

            button_layout = QHBoxLayout()
            for i in range(count):
                button = QPushButton()
                button_layout.addWidget(button)
            main_layout.addLayout(button_layout)

            info_label = QLabel("viwobnowb")

            basement_label = QLabel("hvowhvnpw")

            main_layout.addWidget(info_label)
            main_layout.addWidget(basement_label)

        elif(type == 1):
            main_layout = QVBoxLayout()

            query_label = QLabel("cubbnkn")

            self.ansver = QLineEdit()

            main_layout.addWidget(query_label)
            main_layout.addWidget(self.ansver)