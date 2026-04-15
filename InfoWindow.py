from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QWizardPage,
                               QGroupBox, QPushButton, QLabel)

class InfoPage(QWizardPage):
    def __init__(self, count, number, text1, text2):
        super().__init__()
        self.text1 = text1
        self.text2 = text2
        self.count = count
        self.number = number

        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        for i in range(count):
            button = QPushButton()
            button_layout.addWidget(button)
        main_layout.addLayout(button_layout)

        info_label = QLabel(text1)

        basement_label = QLabel(text2)

        main_layout.addWidget(info_label)
        main_layout.addWidget(basement_label)

        self.setLayout(main_layout)
