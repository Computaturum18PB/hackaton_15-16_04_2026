from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QWizard)

import InfoWindow
from Shablon import Shablon


class BaseWizard1(QWizard):
    def __init__(self, count, list, info, image, parent=None):
        super().__init__(parent)
        self.count = count
        self.list = list
        self.info = info
        self.image = image
        self.setWindowTitle("Курс химии")
        self.setWizardStyle(QWizard.ModernStyle)

        for i in range(count):
            page = Shablon(count, i, self.list, self.info, self.image)
            self.addPage(page)

        self.setButtonText(QWizard.FinishButton, "Закончить")