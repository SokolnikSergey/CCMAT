from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal

class LangButton(QLabel):
    languageChanged = pyqtSignal(str)
    def __init__(self):
        super(LangButton, self).__init__()
        self.__langs = {}
        self.__current_lang = 0
        self.setStyleSheet("text-align: center;")

    def add_language(self, lang, lang_img):
        self.__langs.update({lang: lang_img})
        self.change_language()

    def mousePressEvent(self, event):
        self.change_language()

    def change_language(self):
        self.__current_lang += 1
        self.__current_lang = self.__current_lang % len(self.__langs.values())
        self.setText("<img src=\""+list(self.__langs.values())[self.__current_lang]+"\">")
        self.languageChanged.emit(list(self.__langs.keys())[self.__current_lang])