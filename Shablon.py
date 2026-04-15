from PySide6.QtWidgets import (QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QWizardPage,
                               QGroupBox, QPushButton, QLabel, QLineEdit)
from PySide6.QtGui import QPixmap, Qt
import markdown

def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

class Shablon(QWizardPage):
    def __init__(self, count, number, type):
        super().__init__()
        self.count = count
        self.number = number
        self.pages = ["lesson1.md"]
        self.pictures = ["oil.jpeg"]
        self.index_page = 0
        self.index_picture = 0

        if (type == 0):            
            main_layout = QVBoxLayout()

            button_layout = QHBoxLayout()
            for i in range(count):
                button = QPushButton()
                button_layout.addWidget(button)
            main_layout.addLayout(button_layout)
            
            text = load_file("course\data\\" + self.pages[self.index_page])
            markdown_text = markdown.markdown(text)

            info_label = QLabel(markdown_text)
            info_label.setWordWrap(True)
            info_label.setTextFormat(Qt.RichText)
            basement_label = QLabel()

            main_layout.addWidget(info_label)
            main_layout.addWidget(basement_label)
            self.setLayout(main_layout)

        elif (type == 1):
            main_layout = QVBoxLayout()
            
            button_layout = QHBoxLayout()
            for i in range(count):
                button = QPushButton()
                button_layout.addWidget(button)
            main_layout.addLayout(button_layout)

            query_label = QLabel("cubbnkn")

            self.ansver = QLineEdit()

            main_layout.addWidget(query_label)
            main_layout.addWidget(self.ansver)
            self.setLayout(main_layout)
    
        elif (type == 2):            
            main_layout = QVBoxLayout()
            
            button_layout = QHBoxLayout()
            for i in range(count):
                button = QPushButton()
                button_layout.addWidget(button)
            main_layout.addLayout(button_layout)
            
            image = QPixmap("course\images\\" + self.pictures[self.index_picture])
            image_label = QLabel(self)
            image_label.setPixmap(image)
            
            main_layout.addWidget(image_label)
            self.setLayout(main_layout)