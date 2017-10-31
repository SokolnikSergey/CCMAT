from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.Qt import Qt, pyqtSignal
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont, QFontDatabase

import TEXT_CONSTANTS

class WarningUI(QWidget):
    on_timeout = pyqtSignal()
    on_ok = pyqtSignal()
    on_cancel = pyqtSignal()

    def __init__(self):
        super(WarningUI, self).__init__()
        self.createObjects()
        self.configObjects()

    def createObjects(self):
        self.__label = QLabel()
        self.__label_logo = QLabel()
        self.__button_ok = QPushButton(TEXT_CONSTANTS.WARNING_WINDOW_OK_BUTTON)
        self.__button_cancel = QPushButton(TEXT_CONSTANTS.WARNING_WINDOW_CANCEL_BUTTON)
        self.__vlay_root = QVBoxLayout()
        self.__hlay_buttons = QHBoxLayout()
        self.__timer = QTimer()



    def configObjects(self):


        id = QFontDatabase.addApplicationFont("fonts/Ubuntu-R.ttf")
        ubuntu_font = QFont(QFontDatabase.applicationFontFamilies(id)[0], 22)

        self.setLayout(self.__vlay_root)
        self.__vlay_root.addSpacing(40)
        self.__vlay_root.addWidget(self.__label_logo)
        self.__vlay_root.addStretch(0)
        self.__vlay_root.addWidget(self.__label)
        self.__vlay_root.addStretch(0)
        self.__vlay_root.addLayout(self.__hlay_buttons)

        self.__hlay_buttons.addWidget(self.__button_ok)
        self.__hlay_buttons.addWidget(self.__button_cancel)

        self.__button_ok.setStyleSheet("QPushButton {border: none; background: green; color: white }"
                                        "QPushButton:pressed { background: black; }")
        self.__button_cancel.setStyleSheet("QPushButton {border: none; background: gray; color: white }"
                                        "QPushButton:pressed { background: black; }")

        self.__vlay_root.setAlignment(Qt.AlignCenter)

        self.__button_ok.setMinimumHeight(80)
        self.__button_cancel.setMinimumHeight(80)
        self.__label.setAlignment(Qt.AlignCenter)

        self.__label.setFont(ubuntu_font)
        self.__button_ok.setFont(ubuntu_font)
        self.__button_cancel.setFont(ubuntu_font)
        self.__button_ok.clicked.connect(self.on_ok)
        self.__button_cancel.clicked.connect(self.on_cancel)

        self.__label.setWordWrap(True)
        self.__label_logo.setAlignment(Qt.AlignCenter)

        self.__timer.timeout.connect(self.on_timeout_slot)



    def setLogo(self, logo):
        self.__label_logo.setText(logo)

    def setText(self, text):
        self.__label.setText(text)

    def startTimer(self, millisecs):
        self.__timer.stop()
        self.__timer.start(millisecs)

    def stopTimer(self):
        self.__timer.stop()

    def on_timeout_slot(self):
        if(self.isHidden()):
            self.__label.setText(TEXT_CONSTANTS.WARNING_WINDOW_TEXT1)
            self.on_timeout.emit()
        elif(not self.isHidden() and self.__label.text() == TEXT_CONSTANTS.WARNING_WINDOW_TEXT1):
            self.on_cancel.emit()

    def getText(self):
        return self.__label.text()
