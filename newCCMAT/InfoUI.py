from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.Qt import Qt
import TEXT_CONSTANTS
class InfoUI(QWidget):

    def __init__(self):
        super(InfoUI, self).__init__()
        self.createObjects()
        self.configObjects()

    def createObjects(self):

        self.__vlay_root = QVBoxLayout()
        self.__button_back = QPushButton("< Назад")
        self.__label_info = QLabel(TEXT_CONSTANTS.INFO_WINDOW_HELP)

    def configObjects(self):
        id = QFontDatabase.addApplicationFont("fonts/Ubuntu-R.ttf")
        ubuntu_font = QFont(QFontDatabase.applicationFontFamilies(id)[0], 15)

        self.setLayout(self.__vlay_root)

        self.__vlay_root.addWidget(self.__button_back)
        self.__vlay_root.addWidget(self.__label_info)
        self.__vlay_root.setContentsMargins(0, 0, 0, 0)

        self.__button_back.setStyleSheet("QPushButton { color: black; border: none; }"
                                         "QPushButton:pressed { background: black; color: white; }")
        self.__button_back.setMinimumHeight(50)
        self.__button_back.setFixedWidth(100)
        self.__button_back.setFont(ubuntu_font)
        self.__button_back.clicked.connect(self.on_button_back)

        self.__label_info.setAlignment(Qt.AlignCenter)
        self.__label_info.setWordWrap(True)
        self.__label_info.setFont(ubuntu_font)

    def setInfoText(self, text):
        self.__label_info.setText(text)

    def on_button_back(self):
        self.deleteLater()