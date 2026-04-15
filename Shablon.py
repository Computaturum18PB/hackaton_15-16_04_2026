from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QWizardPage,
                               QGroupBox, QPushButton, QLabel, QLineEdit, QCheckBox)
from PySide6.QtGui import QPixmap, Qt
import markdown

def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

class Shablon(QWizardPage):
    def __init__(self, count, number, list):
        super().__init__()
        self.count = count
        self.number = number
        self.list = list
        self.pages = ["lesson1.md", "lesson2.md", "lesson3.md"]
        self.pictures = ["oil.jpeg", "sheme.png", "omg.png"]

        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        for i in range(count):
            button = QPushButton()
            button_layout.addWidget(button)
        main_layout.addLayout(button_layout)

        if(self.list[number] == 0):
            text = load_file("course\\data\\" + self.pages[self.number])
            markdown_text = markdown.markdown(text)

            info_label = QLabel(markdown_text)
            info_label.setWordWrap(True)
            info_label.setTextFormat(Qt.RichText)
            basement_label = QLabel()

            main_layout.addWidget(info_label)
            main_layout.addWidget(basement_label)
            self.setLayout(main_layout)

        if(self.list[number] == 1):
            text = load_file("course\\data\\" + self.pages[self.number])

            text_query = text.split("\n")[0]
            text_answer_1 = text.split("\n")[1]
            text_answer_2 = text.split("\n")[2]
            text_answer_3 = text.split("\n")[3]
            text_answer_4 = text.split("\n")[4]
            self.answer = text.split("\n")[5]

            markdown_text_query = markdown.markdown(text_query)
            markdown_text_answer_1 = markdown.markdown(text_answer_1)
            markdown_text_answer_2 = markdown.markdown(text_answer_2)
            markdown_text_answer_3 = markdown.markdown(text_answer_3)
            markdown_text_answer_4 = markdown.markdown(text_answer_4)

            query_label = QLabel(markdown_text_query)
            group_layout = QGroupBox()

            self.answer1 = QCheckBox(markdown_text_answer_1)
            self.answer2 = QCheckBox(markdown_text_answer_2)
            self.answer3 = QCheckBox(markdown_text_answer_3)
            self.answer4 = QCheckBox(markdown_text_answer_4)

            group_layout.addWidget(self.answer1)
            group_layout.addWidget(self.answer2)
            group_layout.addWidget(self.answer3)
            group_layout.addWidget(self.answer4)

            main_layout.addWidget(query_label)
            main_layout.addWidget(group_layout)
            self.setLayout(main_layout)
    
        if (self.list[self.number] == 2):
            image = QPixmap("course\\images\\" + self.pictures[self.number])
            image_label = QLabel(self)
            image_label.setPixmap(image)
            
            main_layout.addWidget(image_label)
            self.setLayout(main_layout)
