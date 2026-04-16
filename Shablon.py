from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QWizardPage,
                               QGroupBox, QPushButton, QLabel, QLineEdit, QCheckBox,
                               QRadioButton, QButtonGroup, QMessageBox, QScrollArea)
from PySide6.QtGui import QPixmap, Qt
import markdown
import os

def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

class Shablon(QWizardPage):
    def __init__(self, count, number, list, info, image, course_path="course"):
        super().__init__()
        self.count = count
        self.number = number
        self.list = list
        self.pages = info
        self.pictures = image
        self.course_path = course_path

        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        for i in range(count):
            button = QPushButton()
            button_layout.addWidget(button)
        main_layout.addLayout(button_layout)

        if(self.list[number] == 0):
            # Используем путь к курсу
            file_path = os.path.join(self.course_path, "data", self.pages[self.number])
            text = load_file(file_path)
            markdown_text = markdown.markdown(text)

            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            content_widget = QWidget()
            content_layout = QVBoxLayout(content_widget)

            info_label = QLabel(markdown_text)
            info_label.setWordWrap(True)
            info_label.setTextFormat(Qt.RichText)
            info_label.setMinimumHeight(500)

            basement_label = QLabel()

            content_layout.addWidget(info_label)
            content_layout.addWidget(basement_label)
            content_layout.addStretch()

            scroll.setWidget(content_widget)

            main_layout.addWidget(scroll)
            self.setLayout(main_layout)

        if(self.list[number] == 1):
            file_path = os.path.join(self.course_path, "data", self.pages[self.number])
            text = load_file(file_path)
            
            text_query = text.split("\n")[0]
            text_answer_1 = text.split("\n")[1]
            text_answer_2 = text.split("\n")[2]
            text_answer_3 = text.split("\n")[3]
            text_answer_4 = text.split("\n")[4]
            self.correct_answer = int(text.split("\n")[5])

            markdown_text_query = markdown.markdown(text_query)
            markdown_text_answer_1 = markdown.markdown(text_answer_1)
            markdown_text_answer_2 = markdown.markdown(text_answer_2)
            markdown_text_answer_3 = markdown.markdown(text_answer_3)
            markdown_text_answer_4 = markdown.markdown(text_answer_4)

            query_label = QLabel(markdown_text_query)
            group_box = QGroupBox("Выберите ответ")

            group_layout = QVBoxLayout()
            group_box.setLayout(group_layout)

            self.answer1 = QRadioButton(markdown_text_answer_1)
            self.answer2 = QRadioButton(markdown_text_answer_2)
            self.answer3 = QRadioButton(markdown_text_answer_3)
            self.answer4 = QRadioButton(markdown_text_answer_4)
            self.buttonAnswer = QPushButton("Проверить")

            self.answer_group = QButtonGroup()
            self.answer_group.addButton(self.answer1, 1)
            self.answer_group.addButton(self.answer2, 2)
            self.answer_group.addButton(self.answer3, 3)
            self.answer_group.addButton(self.answer4, 4)

            group_layout.addWidget(self.answer1)
            group_layout.addWidget(self.answer2)
            group_layout.addWidget(self.answer3)
            group_layout.addWidget(self.answer4)
            group_layout.addWidget(self.buttonAnswer)

            self.buttonAnswer.clicked.connect(self.check_answer)

            main_layout.addWidget(query_label)
            main_layout.addWidget(group_box)
            self.setLayout(main_layout)
    
        if (self.list[self.number] == 2):
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

            content_widget = QWidget()
            content_layout = QVBoxLayout(content_widget)

            target_height = 400

            image_path = os.path.join(self.course_path, "images", self.pictures[self.number])
            image = QPixmap(image_path)
            scaled_image = image.scaledToHeight(target_height, Qt.SmoothTransformation)
            image_label = QLabel(self)
            image_label.setPixmap(scaled_image)

            image_size = scaled_image.size()
            page_width = image_size.width() + 100
            page_height = image_size.height() + 150
            self.setFixedSize(page_width, page_height)

            legend_label = QLabel()
            legend_label.setWordWrap(True)
            legend_label.setTextFormat(Qt.RichText)

            content_layout.addWidget(image_label)
            content_layout.addWidget(legend_label)

            scroll.setWidget(content_widget)

            main_layout.addWidget(scroll)
            self.setLayout(main_layout)

    def check_answer(self):
        """Проверка правильности ответа"""
        selected_id = self.answer_group.checkedId()

        if selected_id == -1:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите ответ!")
            return

        if selected_id == self.correct_answer:
            QMessageBox.information(self, "Результат", "Правильно! Молодец!😉")
        else:
            QMessageBox.information(self, "Результат", "Неправильно! Попробуйте снова!☹️")

            self.answer_group.setExclusive(False)
            self.answer1.setChecked(False)
            self.answer2.setChecked(False)
            self.answer3.setChecked(False)
            self.answer4.setChecked(False)
            self.answer_group.setExclusive(True)