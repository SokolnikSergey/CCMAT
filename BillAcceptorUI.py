from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt


class BillAcceptorUI(QWidget):

    def __init__(self):
        super(BillAcceptorUI, self).__init__()
        self.createObjects()
        self.configObjects()

    def createObjects(self):
        self.__vlay_main = QVBoxLayout()

        self.__label_enter_money = QLabel("Вставьте купюру<br><br><img src=\"images/cash.png\">")

    def configObjects(self):

        self.setLayout(self.__vlay_main)

        self.__vlay_main.addWidget(self.__label_enter_money)
        self.__vlay_main.setContentsMargins(0, 0, 0, 0)

        self.__label_enter_money.setFont(QFont("Segoe UI", 15))
        self.__label_enter_money.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("background: rgb(66, 101, 244); color: white;")

