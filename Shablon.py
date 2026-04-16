from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QWizardPage,
                               QGroupBox, QPushButton, QLabel, QLineEdit, QCheckBox,
                               QRadioButton, QButtonGroup, QMessageBox, QScrollArea,
                               QSizePolicy)
from PySide6.QtGui import QPixmap, Qt, QIcon
from PySide6.QtCore import QSize
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

        image_layout = QHBoxLayout()
        for i in range(count):

            if list[i] == 0:
                if i <= number:
                    image = QPixmap("images\\done_theory.png")
                else:
                    image = QPixmap("images\\undone_theory.png")
            elif list[i] == 1:
                if i <= number:
                    image = QPixmap("images\\done_test.png")
                else:
                    image = QPixmap("images\\undone_test.png")
            else:
                if i <= number:
                    image = QPixmap("images\\done_image.png")
                else:
                    image = QPixmap("images\\undone_image.png")
            image_label = QLabel()
            image_label.setPixmap(image)
            image_layout.addWidget(image_label)

        main_layout.addLayout(image_layout)

        if(self.list[number] == 0):
            # Используем путь к курсу
            file_path = os.path.join(self.course_path, "data", self.pages[self.number])
            text = load_file(file_path)
            markdown_text = markdown.markdown(text)

            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            main_layout.addWidget(scroll, 1)

            content_widget = QWidget()
            content_layout = QVBoxLayout(content_widget)

            info_label = QLabel(markdown_text)
            info_label.setWordWrap(True)
            info_label.setTextFormat(Qt.RichText)
            info_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            basement_label = QLabel()

            content_layout.addWidget(info_label)
            content_layout.addWidget(basement_label)
            content_layout.addStretch()

            scroll.setWidget(content_widget)

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

        if self.list[self.number] == 2:

            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            content_widget = QWidget()
            content_layout = QVBoxLayout(content_widget)
            content_layout.setContentsMargins(0, 0, 0, 0)

            image_path = os.path.join(self.course_path, "images", self.pictures[self.number])
            image = QPixmap(image_path)

            image_label = QLabel()
            image_label.setAlignment(Qt.AlignCenter)
            image_label.setScaledContents(True)

            self.original_pixmap = image
            image_label.setPixmap(image)

            image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            legend_label = QLabel()
            legend_label.setWordWrap(True)
            legend_label.setTextFormat(Qt.RichText)
            legend_label.setAlignment(Qt.AlignCenter)

            if self.pages[self.number] != "":
                file_path = os.path.join(self.course_path, "data", self.pages[self.number])
                text = load_file(file_path)
                markdown_text = markdown.markdown(text)
                legend_label.setText(markdown_text)

            content_layout.addWidget(image_label, 1)
            content_layout.addWidget(legend_label, 0)

            scroll.setWidget(content_widget)
            main_layout.addWidget(scroll)
            self.setLayout(main_layout)

        def resizeEvent(self, event):
            super().resizeEvent(event)
            if hasattr(self, 'original_pixmap'):
                available_width = self.width() - 50
                available_height = self.height() - 100

                scaled = self.original_pixmap.scaled(
                    available_width, available_height,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                self.image_label.setPixmap(scaled)

    def check_answer(self):
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