from PySide6.QtCore import QFile, Qt, Slot
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFileDialog, QHBoxLayout, QListWidget, QListWidgetItem, QRadioButton, QWidget, QVBoxLayout,
                               QLabel, QGridLayout, QPushButton, QMessageBox)
from PySide6.QtGui import QIcon, QPixmap
import os
import shutil

from BaseWindow import BaseWizard1


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.list_types = []
        self.files_info = []  
        self.files_image = []  
        self.course_folder = "user_course" 

        if not os.path.exists(self.course_folder):
            os.makedirs(self.course_folder)
        if not os.path.exists(os.path.join(self.course_folder, "data")):
            os.makedirs(os.path.join(self.course_folder, "data"))
        if not os.path.exists(os.path.join(self.course_folder, "images")):
            os.makedirs(os.path.join(self.course_folder, "images"))

        self.setWindowTitle("Спектр")
        
        self.setWindowIcon(QIcon(QPixmap("images/app_icon.ico")))
        self.resize(1200, 800)

        main_layuot = QVBoxLayout()

        title_label = QLabel("Добро пожаловать в приложение Спектр! Вы можете выбрать наш авторский курс или загрузить свой! Приятного обучения!😁")
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
        
        button_create_course = QPushButton("Создать курс")
        button_create_course.clicked.connect(self.create_course)
        
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
        main_layuot.addWidget(button_create_course)

        self.setLayout(main_layuot)

    @Slot()
    def start_ready_course(self):
        list_types = [0, 2, 1, 1, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1]  
        info = ["lesson1.md", "", "test1.md", "test2.md", "test3.md", "lesson2.md", "", "lesson3.md", "", "lesson4.md", "lesson5.md", "lesson6.md", "lesson7.md", "lesson8.md", "practice1.md", "test4.md", "test5.md", "test6.md"] 
        image = ["", "image1.jpeg", "", "", "", "", "image2.png", "", "image3.png", "", "", "", "", "", "", "", "", ""]
        
        wizard = BaseWizard1(len(list_types), list_types, info, image, self, "course", "images/icon.png")
        wizard.show()
    
    @Slot()
    def add_element(self):
        if self.radio_button_theory.isChecked():
            file_filter = "*.md"
            dialog_title = "Выберите файл теории .md"
            icon_text = "📄 - файл теории"
            self.list_types.append(0)
            target_folder = os.path.join(self.course_folder, "data")
        elif self.radio_button_image.isChecked():
            file_filter = "*.jpg *.jpeg *.png"
            dialog_title = "Выберите файл картинки .png/.jpeg/.jpg"
            icon_text = "🖼️ - файл картинки"
            self.list_types.append(2)
            target_folder = os.path.join(self.course_folder, "images")
        elif self.radio_button_test.isChecked():
            file_filter = "*.md"
            dialog_title = "Выберите файл теста .md"
            icon_text = "🧪 - файл теста"
            self.list_types.append(1)
            target_folder = os.path.join(self.course_folder, "data")
        elif self.radio_button_interactive.isChecked():
            QMessageBox.information(self, "Информация", "Интерактивный режим пока не реализован")
            return
        else:
            return

        file_path, _ = QFileDialog.getOpenFileName(self, dialog_title, filter=file_filter)
        
        if not file_path:
            if self.list_types:
                self.list_types.pop()
            return
        
        file_name = os.path.basename(file_path)
        unique_name = f"{len(self.list_types)-1}_{file_name}"
        target_path = os.path.join(target_folder, unique_name)
        shutil.copy2(file_path, target_path)
        
        if self.radio_button_theory.isChecked() or self.radio_button_test.isChecked():
            self.files_info.append(unique_name)
            self.files_image.append("")  
        elif self.radio_button_image.isChecked():
            self.files_info.append("")
            self.files_image.append(unique_name)  
        
        item = QWidget()
        item_layout = QHBoxLayout(item)
        item_layout.setContentsMargins(5, 5, 5, 5)
        
        icon_label = QLabel(icon_text)
        text_label = QLabel(file_name)
        
        delete_item_button = QPushButton()
        delete_item_button.setIcon(QPixmap("images/trash.png"))
        delete_item_button.setFixedSize(20, 20)
        delete_item_button.clicked.connect(lambda checked, fp=unique_name, idx=len(self.files_info)-1: self.remove_file(fp, idx))
        
        item_layout.addWidget(icon_label)
        item_layout.addWidget(text_label)
        item_layout.addStretch()
        item_layout.addWidget(delete_item_button)
        
        list_item = QListWidgetItem(self.add_course)
        list_item.setSizeHint(item.sizeHint())
        self.add_course.addItem(list_item)
        self.add_course.setItemWidget(list_item, item)
        
        list_item.setData(Qt.UserRole, unique_name)

    @Slot()
    def remove_file(self, file_name, index):
        if 0 <= index < len(self.list_types):
            file_type = self.list_types[index]
            if file_type in [0, 1]: 
                file_path = os.path.join(self.course_folder, "data", file_name)
            else: 
                file_path = os.path.join(self.course_folder, "images", file_name)
            
            if os.path.exists(file_path):
                os.remove(file_path)
        
        if 0 <= index < len(self.list_types):
            self.list_types.pop(index)
        if 0 <= index < len(self.files_info):
            self.files_info.pop(index)
        if 0 <= index < len(self.files_image):
            self.files_image.pop(index)
            
        for i in range(self.add_course.count()):
            item = self.add_course.item(i)
            if item.data(Qt.UserRole) == file_name:
                self.add_course.takeItem(i)
                break
    
    @Slot()
    def create_course(self):
        if len(self.list_types) == 0:
            QMessageBox.warning(self, "Ошибка", "Добавьте хотя бы один файл для создания курса!")
            return
        
        list_types = self.list_types.copy()
        info = self.files_info.copy()
        image = self.files_image.copy()
        
        wizard = BaseWizard1(len(list_types), list_types, info, image, self, self.course_folder)
        wizard.show()

def load_stylesheet(app):
    style_file = QFile("styles/main.qss")
    if style_file.open(QFile.ReadOnly | QFile.Text):
        stylesheet = style_file.readAll().data().decode('utf-8')
        app.setStyleSheet(stylesheet)
        style_file.close()
        return True
    return False


if __name__ == "__main__":
    app = QApplication()
    if not load_stylesheet(app):
        print("Не удалось загрузить файл стилей styles/main.qss")
    
    window = MainWindow()
    window.show()
    app.exec()