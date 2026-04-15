from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFileDialog, QHBoxLayout, QListWidget, QListWidgetItem, QRadioButton, QWidget, QVBoxLayout,
                               QLabel, QGridLayout, QPushButton)
from PySide6.QtGui import QIcon, QPixmap
import os

from BaseWindow import BaseWizard1


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("____")
        
        self.setWindowIcon(QIcon(QPixmap("images/icon.png")))
        self.showMaximized()

        main_layuot = QVBoxLayout()

        title_label = QLabel("Добро пожаловать в приложение ____! Вы можете выбрать наш авторский курс или загрузить свой! Приятного обучения!😁")
        title_label.setWordWrap(True)

        author_course = QLabel("Авторский обучающий курс: \"Переработка нефти\"")

        button_author_course = QPushButton("Перейти")
        button_author_course.clicked.connect(self.start_ready_course)
        
        describe_add_course = QLabel("Или можете файлы и собрать курс самостоятельно: ")
        
        self.add_course = QListWidget()
        
        self.radio_button_theory = QRadioButton("Теория")
        self.radio_button_theory.setChecked(True)
        
        self.radio_button_image = QRadioButton("Картинка")
        
        self.radio_button_test = QRadioButton("Тест")
        
        self.radio_button_interactive = QRadioButton("Интерактив")
        
        group_radio_buttons = QButtonGroup()
        group_radio_buttons.addButton(self.radio_button_theory)
        group_radio_buttons.addButton(self.radio_button_image)
        group_radio_buttons.addButton(self.radio_button_test)
        group_radio_buttons.addButton(self.radio_button_interactive)
        
        button_add_file = QPushButton("Добавить файл")
        button_add_file.clicked.connect(self.add_element)
        
        main_layuot.addWidget(title_label)
        main_layuot.addWidget(author_course)
        main_layuot.addWidget(button_author_course)
        main_layuot.addWidget(describe_add_course)
        main_layuot.addWidget(self.add_course)
        main_layuot.addWidget(self.radio_button_theory)
        main_layuot.addWidget(self.radio_button_image)
        main_layuot.addWidget(self.radio_button_test)
        main_layuot.addWidget(self.radio_button_interactive)
        main_layuot.addWidget(button_add_file)

        self.setLayout(main_layuot)

    @Slot()
    def start_theme_1(self):
        list = [0, 1, 2]
        info = ["lesson1.md", "lesson2.md", "test1.md"]
        image = ["oil.jpeg", "sheme.png", "omg.png"]
        wizard = BaseWizard1(len(list), list, info, image, self)
        wizard.show()
    
    @Slot()
    def add_element(self):
        if self.radio_button_theory.isChecked():
            file_filter = "*.md"
            dialog_title = "Выберите файл теории .md"
            icon_text = "📄 - файл теории"
        elif self.radio_button_image.isChecked():
            file_filter = "*.jpg *.jpeg *.png"
            dialog_title = "Выберите файл картинки .png/.jpeg/.jpg"
            icon_text = "🖼️ - файл картинки"
        elif self.radio_button_test.isChecked():
            file_filter = "*.md"
            dialog_title = "Выберите файл теста .md"
            icon_text = "🧪 - файл теста"
        elif self.radio_button_interactive.isChecked():
            pass
        else:
            return

        file_path, _ = QFileDialog.getOpenFileName(self, dialog_title, filter=file_filter)
        
        if not file_path:
            return
        
        item = QWidget()
        item_layout = QHBoxLayout(item)
        item_layout.setContentsMargins(5, 5, 5, 5)
        
        icon_label = QLabel(icon_text)
        text_label = QLabel(os.path.basename(file_path))
        

        delete_item_button = QPushButton()
        delete_item_button.setIcon(QPixmap("images/trash.png"))
        delete_item_button.setFixedSize(20, 20)
        delete_item_button.clicked.connect(lambda checked, fp=file_path: self.remove_file(fp))
        
        item_layout.addWidget(icon_label)
        item_layout.addWidget(text_label)
        item_layout.addStretch()
        item_layout.addWidget(delete_item_button)
        

        list_item = QListWidgetItem(self.add_course)
        list_item.setSizeHint(item.sizeHint())
        self.add_course.addItem(list_item)
        self.add_course.setItemWidget(list_item, item)
        
        list_item.setData(Qt.UserRole, file_path)

    @Slot()
    def remove_file(self, file_path):
        for i in range(self.add_course.count()):
            item = self.add_course.item(i)
            if item.data(Qt.UserRole) == file_path:
                self.add_course.takeItem(i)
                break


app = QApplication()
window = MainWindow()
window.show()
app.exec()