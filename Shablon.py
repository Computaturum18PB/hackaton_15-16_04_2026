from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QWizardPage,
                               QGroupBox, QPushButton, QLabel, QLineEdit, QCheckBox,
                               QRadioButton, QButtonGroup, QMessageBox, QScrollArea)
from PySide6.QtGui import QPixmap, Qt
# import markdown

def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

class Shablon(QWizardPage):
    def __init__(self, count, number, list, info, image):
        super().__init__()
        self.count = count
        self.number = number
        self.list = list
        self.pages = info
        self.pictures = image

        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        for i in range(count):
            button = QPushButton()
            button_layout.addWidget(button)
        main_layout.addLayout(button_layout)

        if(self.list[number] == 0):
            # text = load_file("course\\data\\" + self.pages[self.number])
            # markdown_text = markdown.markdown(text)

            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            content_widget = QWidget()
            content_layout = QVBoxLayout(content_widget)

            info_label = QLabel("jjjjjj jjjjjjj jjjjjjjjj jjjjjj jjjjjj"
                                "jjjjjj jjjjjjjj jjjjjjjj jjjjjj jjjj jjj"
                                "jjjjjjj jjjj jjjjjjjj jjjjjjjjj jj jj jjjjjjjj"
                                "jjj jj  j jjj jjjj jjjjjjjj jjjjjjjj jjjjjjjjj jjj"
                                "jjjjjjjj jjjjj jjjjjjj jjjjjjj jjjj jjjjjj j jjj jjjjjjj jjjjjjjjjjjjjjj jjjjjjjj jjjjjjjjj jjjjjjjjjjj jjjjjjjjjjj jjjjjjjjj jjjj cwbvowvno nqovn vnqonvpqvnpqv vnpqvnp2nvmp2bvmp2b bn2pnbp2mbp2mbp2mbp2mbp2mbp2b vn2pnp2mnbp2mbp2mbp2vnp2m vn2pvn2pvp2vm2pvm2pvm2pvm mvp2mvp2vm2pvmp2vmp2vmp2m vp2mvp2mvp2mvp2mvp2mv vmp2vmp2vmp2vmp2vmp2v vm2pvm2pvmp2mvp2mvp2vmp2mv bqiwbvoqboqbowqbnownbowinbow nvqoboqnvboqnboqnboqnboqnbo vnovnovno2vno2vnownvownvow vnownvownvownvownvownvownv nvownvownvownvownvownvownvown wvnowvnowvnowvnownvownvownv vn wovnwovnownvownvownv vnwovnovnonvownv vnwovnwonvownvow vnwovnownvownvownv vnwovnwovnownvownvow bwi vbiwbviw viwbvibwvi vivbi2vb2ibvi2 vbi2vbi2vbi2v vb2ivbi32bvi3v 3vb i3vbi3vb2 vi2vbi ibi2 2i bi3bibib2ighbvbi2 iv 3bv 2vi3v i3v 3vb 3ii3vb")

            # info_label = QLabel(markdown_text)
            info_label.setWordWrap(True)
            info_label.setTextFormat(Qt.RichText)
            # info_label.setMinimumHeight(500)

            basement_label = QLabel()

            content_layout.addWidget(info_label)
            content_layout.addWidget(basement_label)
            # content_layout.addStretch()

            scroll.setWidget(content_widget)

            main_layout.addWidget(scroll)
            self.setLayout(main_layout)

        if(self.list[number] == 1):
            # text = load_file("course\\data\\" + self.pages[self.number])
            #
            # text_query = text.split("\n")[0]
            # text_answer_1 = text.split("\n")[1]
            # text_answer_2 = text.split("\n")[2]
            # text_answer_3 = text.split("\n")[3]
            # text_answer_4 = text.split("\n")[4]
            # self.answer = text.split("\n")[5]

            # markdown_text_query = markdown.markdown(text_query)
            # markdown_text_answer_1 = markdown.markdown(text_answer_1)
            # markdown_text_answer_2 = markdown.markdown(text_answer_2)
            # markdown_text_answer_3 = markdown.markdown(text_answer_3)
            # markdown_text_answer_4 = markdown.markdown(text_answer_4)

            # query_label = QLabel(markdown_text_query)
            group_box = QGroupBox("Выберите ответы")  # можно добавить заголовок

            group_layout = QVBoxLayout()
            group_box.setLayout(group_layout)
            #
            # self.answer1 = QCheckBox(markdown_text_answer_1)
            # self.answer2 = QCheckBox(markdown_text_answer_2)
            # self.answer3 = QCheckBox(markdown_text_answer_3)
            # self.answer4 = QCheckBox(markdown_text_answer_4)
            #
            # group_layout.addWidget(self.answer1)
            # group_layout.addWidget(self.answer2)
            # group_layout.addWidget(self.answer3)
            # group_layout.addWidget(self.answer4)

            query_label = QLabel("3")
            group_box = QGroupBox("Выберите ответы")  # можно добавить заголовок

            group_layout = QVBoxLayout()
            group_box.setLayout(group_layout)

            self.answer = 3
            self.answer1 = QRadioButton("Вариант ответа 1")
            self.answer2 = QRadioButton("Вариант ответа 2")
            self.answer3 = QRadioButton("Вариант ответа 3")
            self.answer4 = QRadioButton("Вариант ответа 4")
            self.buttonAnswer = QPushButton("проверить")

            self.answer_group = QButtonGroup()
            self.answer_group.addButton(self.answer1, 1)  # ID = 1
            self.answer_group.addButton(self.answer2, 2)  # ID = 2
            self.answer_group.addButton(self.answer3, 3)  # ID = 3
            self.answer_group.addButton(self.answer4, 4)  # ID = 4

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

            image = QPixmap("course\\images\\" + self.pictures[self.number])
            # text = load_file("course\\data\\" + self.pages[self.number])
            # markdown_text = markdown.markdown(text)
            image_label = QLabel(self)
            image_label.setPixmap(image)

            # legend_label = QLabel(markdown_text)
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

        if selected_id == -1:  # ничего не выбрано
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите ответ!")
            return

        if selected_id == self.answer:
            QMessageBox.information(self, "Результат", "Правильно!")
            # Действие при правильном ответе
        else:
            QMessageBox.information(self, "Результат", "Неправильно!")

            self.answer_group.setExclusive(False)
            self.answer1.setChecked(False)
            self.answer2.setChecked(False)
            self.answer3.setChecked(False)
            self.answer4.setChecked(False)
            self.answer_group.setExclusive(True)