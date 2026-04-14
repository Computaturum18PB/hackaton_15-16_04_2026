# Заметки - справочник функций библиотеки Qt

## Основные виджеты

- `QWidget` - базовый виджет (контейнер);
- `QMainWindow` - главное окно (с меню, статусбаром, центральным виджетом);
- `QLabel` - текстовая метка или изображение;
- `QPushButton` - кнопка;
- `QLineEdit` - однострочное поле ввода;
- `QTextEdit` - многострочное поле ввода;
- `QComboBox` - выпадающий список;
- `QCheckBox` - флажок;
- `QRadioButton` - радиокнопка;
- `QSlider `- ползунок;
- `QProgressBar` - индикатор прогресса;
- `QTableWidget` - таблица;
- `QListWidget` - список;
- `QTreeWidget` - дерево;
- `QTabWidget` - вкладки;
- `QGroupBox` - группировка виджетов;
- `QScrollArea `- прокручиваемая область;

## Макеты 

- `QVBoxLayout()` - вертикальный макет;
- `QHBoxLayout()` - горизонтальный макет;
- `QGridLayout()` - сеточный макет (по строкам и колонкам);
- `layout.addWidget(widget)` - добавление виджета;
- `layout.addWidget(widget, stretch=1) `- с коэффициентом растяжения;
- `layout.addLayout(sub_layout) `- вложенный макет;
- `setLayout(layout)` - установка макета для виджета;
- `setCentralWidget(widget)` - установка центрального виджета в QMainWindow;

## Сигналы и слоты

- `button.clicked.connect(function)` - подключение сигнала к слоту;
- `button.clicked.connect(lambda: print("Clicked"))` - лямбда-функция;
- `lineEdit.textChanged.connect(function)` - сигнал изменения текста;
- `comboBox.currentIndexChanged.connect(function)` - сигнал смены индекса;
- `slider.valueChanged.connect(function)` - сигнал изменения значения;
- `action.triggered.connect(function)` - сигнал действия из меню;
- `QApplication.quit()` - выход из приложения;
- `widget.close()` - закрытие виджета;

## Меню и панели инструментов

- `menubar = self.menuBar()` - получение строки меню;
- `file_menu = menubar.addMenu('&File')` - добавление меню (Alt+F);
- `open_action = QAction('Open', self)` - создание действия;
- `open_action.setShortcut('Ctrl+O')` - установка горячей клавиши;
- `open_action.triggered.connect(self.open_file)` - подключение действия;
- `file_menu.addAction(open_action) `- добавление действия в меню;
- `toolbar = self.addToolBar('Main')` - создание панели инструментов;
- `toolbar.addAction(open_action)` - добавление действия на панель;
- `self.statusBar().showMessage('Ready')` - сообщение в статус-бар;

## Диалоги

- `QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*.*)')` - выбор файла;
- `QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV (*.csv)')` - сохранение файла;
- `QFileDialog.getExistingDirectory(self, 'Select Directory')` - выбор папки;
- `QColorDialog.getColor(initial, self, 'Select Color')` - выбор цвета;
- `QFontDialog.getFont()` - выбор шрифта;
- `QInputDialog.getText(self, 'Input', 'Enter value:')`- ввод текста;
- `QMessageBox.information(self, 'Info', 'Message')` - информационное сообщение;
- `QMessageBox.warning(self, 'Warning', 'Message')` - предупреждение;
- `QMessageBox.question(self, 'Confirm', 'Continue?')` - вопрос с ответом;

## Обработка событий мыши

- `mousePressEvent` - нажатие кнопки; 
- `mouseReleaseEvent` - отпускание;  
- `mouseMoveEvent` - движение с зажатой кнопкой; 
- `mouseDoubleClickEvent` - двойной щелчок; 
- `wheelEvent` - вращение колесика;
- `event.x()`, `event.y()` - локальные координаты виджета;
- `event.globalX()`, `event.globalY()` - экранные координаты;
- `event.modifiers()` - клавиши модификаторы (Qt.ShiftModifier, Qt.ControlModifier, Qt.AltModifier);  
- `event.button()/buttons()` - кнопки мыши с разовым или множественным нажатием (Qt.LeftButton, Qt.RightButton, Qt.MiddleButton); 
- `setMouseTracking(True)` - атрибут отслеживания движения без нажатия;