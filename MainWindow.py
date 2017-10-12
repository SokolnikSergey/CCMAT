from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from Button import ImageButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.Qt import Qt, QSize, pyqtSignal
from BuyCoinsWindow import BuyCoinsWindow
from Button import ImageButton

class MainWindow(QWidget):

    on_close = pyqtSignal(QWidget)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.create_widgets()
        self.prepare_layouts()
        self.config_widgets()

    def create_widgets(self):

        self.__vlay_main = QVBoxLayout()
        self.__hlay_buttons_buy_coins = QHBoxLayout()

        self.__label_logo = QLabel("<img src=\"images/logo.png\">")
        self.__label_select_currency = QLabel(self.tr("Buy"))

        self.button_bitcoin = ImageButton("Bitcoin","images/bitcoin.png")
        self.__button_etherium = ImageButton("Ethereum", "images/ethereum.png")
        self.__button_info = QPushButton(self.tr("Info"))
        self.__button_others_currency = QPushButton(self.tr("Other currencies"))

    def prepare_layouts(self):

        self.__vlay_main.setAlignment(Qt.AlignCenter)
        self.__vlay_main.addWidget(self.__label_logo)
        self.__vlay_main.addWidget(self.__label_select_currency)
        self.__vlay_main.addLayout(self.__hlay_buttons_buy_coins)
        self.__vlay_main.addWidget(self.__button_others_currency)
        self.__vlay_main.addWidget(self.__button_info)

        self.__hlay_buttons_buy_coins.addWidget(self.button_bitcoin)
        self.__hlay_buttons_buy_coins.addWidget(self.__button_etherium)

        self.setLayout(self.__vlay_main)

    def config_widgets(self):
        self.button_bitcoin.setCurrency("112 500 ₴")
        self.__button_etherium.setCurrency("1 234 ₴")
        self.button_bitcoin.setFixedSize(300, 300)
        self.__button_info.setStyleSheet("QPushButton {background: rgb(66, 101, 244); color: white; border-radius: 10px; }"
                                         "QPushButton:pressed { background: black; }")
        self.__button_info.setIcon(QIcon("images/info.png"))
        self.__button_info.setIconSize(QSize(20, 20))

        self.__button_others_currency.setStyleSheet(self.__button_info.styleSheet())

        self.__button_etherium.setFixedSize(self.button_bitcoin.size())

        self.__button_info.setMinimumHeight(50)
        self.__button_info.setFont(QFont("Segoe UI", 15))
        self.__button_others_currency.setMinimumHeight(self.__button_info.minimumHeight())
        self.__button_others_currency.setFont(self.__button_info.font())
        self.__label_logo.setAlignment(Qt.AlignCenter)
        self.__label_select_currency.setFont(self.__button_info.font())
        self.__label_select_currency.setAlignment(Qt.AlignCenter)
        self.__label_select_currency.setMinimumHeight(30)

        self.button_bitcoin.clicked.connect(self.on_crypt_selected)

    def on_crypt_selected(self):
        self.on_close.emit(BuyCoinsWindow())