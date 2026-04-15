from PySide6.QtWidgets import (QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QWizardPage,
                               QGroupBox, QPushButton, QLabel, QLineEdit)
from PySide6.QtGui import QPixmap, Qt
import markdown

def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

class Shablon(QWizardPage):
    def __init__(self, count, number, list, pages, image):
        super().__init__()
        self.count = count
        self.number = number
        self.list = list
        self.pages = pages
        self.pictures = image

        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        for i in range(count):
            button = QPushButton()
            button_layout.addWidget(button)
        main_layout.addLayout(button_layout)

        if(self.list[number] == 0):
            text = load_file("course\data\\" + self.pages[self.number])
            markdown_text = markdown.markdown(text)

            info_label = QLabel(markdown_text)
            info_label.setWordWrap(True)
            info_label.setTextFormat(Qt.RichText)
            basement_label = QLabel()

            main_layout.addWidget(info_label)
            main_layout.addWidget(basement_label)
            self.setLayout(main_layout)

        if(self.list[number] == 1):
            query_label = QLabel()
            group_layout = QGroupBox()

            query_label = QLabel("cubbnkn")

            self.ansver = QLineEdit()

            main_layout.addWidget(query_label)
            main_layout.addWidget(self.ansver)
            self.setLayout(main_layout)
    
        if (self.list[self.number] == 2):
            image = QPixmap("course\images\\" + self.pictures[self.number])
            image_label = QLabel(self)
            image_label.setPixmap(image)
            
            main_layout.addWidget(image_label)
            self.setLayout(main_layout)
