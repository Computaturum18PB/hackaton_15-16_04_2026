from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QWizardPage,
                               QGroupBox, QPushButton, QLabel, QLineEdit)

class Shablon(QWizardPage):
    def __init__(self, count, number, list):
        super().__init__()
        self.count = count
        self.number = number
        self.list = list

        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        for i in range(count):
            button = QPushButton()
            button_layout.addWidget(button)
        main_layout.addLayout(button_layout)

        if(self.list[number] == 0):
            info_label = QLabel()

            basement_label = QLabel()

            main_layout.addWidget(info_label)
            main_layout.addWidget(basement_label)
            self.setLayout(main_layout)

        if(self.list[number] == 1):
            query_label = QLabel()
            group_layout = QGroupBox()
            self.ansver = QLineEdit()

            main_layout.addWidget(query_label)
            main_layout.addWidget(self.ansver)
            self.setLayout(main_layout)
