from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt, pyqtSignal
from BillAcceptorUI import BillAcceptorUI
from QRScannerUI import QRScannerUI
import MainWindow

class BuyCoinsWindow(QWidget):

    on_close = pyqtSignal(QWidget)

    def __init__(self):
        super(BuyCoinsWindow, self).__init__()
        self.createObjects()
        self.prepareLayouts()
        self.configObjects()

    def createObjects(self):

        self.__hlay_main = QHBoxLayout()
        self.__vlay_left = QVBoxLayout()

        self.__widget_bill_acceptor = BillAcceptorUI()
        self.__widget_qr_scanner = QRScannerUI()

        self.__label_enter_wallet = QLabel("Сканирование QR-кода..")

        self.__button_buy = QPushButton("Купить")
        self.__button_back = QPushButton("< Назад")


    def prepareLayouts(self):
        self.__hlay_main.setSpacing(0)
        self.__hlay_main.addLayout(self.__vlay_left)
        self.__hlay_main.addWidget(self.__widget_bill_acceptor)
        self.__hlay_main.setContentsMargins(0, 0, 0, 0)

        self.__vlay_left.addWidget(self.__button_back)
        self.__vlay_left.addWidget(self.__label_enter_wallet)
        self.__vlay_left.addWidget(self.__widget_qr_scanner)
        self.__vlay_left.addWidget(self.__button_buy)
        self.__vlay_left.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.__hlay_main)

    def configObjects(self):

        self.__label_enter_wallet.setFont(QFont("Segoe UI", 15))
        self.__label_enter_wallet.setAlignment(Qt.AlignCenter)
        self.__label_enter_wallet.setWordWrap(True)

        self.__widget_qr_scanner.qr_decoded.connect(self.on_qr_decoded)

        self.__button_back.setFixedWidth(100)
        self.__button_back.setStyleSheet("QPushButton { color: black; border: none; }"
                                         "QPushButton:pressed { background: black; color: white; }")
        self.__button_back.setMinimumHeight(50)
        self.__button_back.setFont(QFont("Segoe UI", 15))
        self.__button_back.clicked.connect(self.on_back_clicked)

        self.__button_buy.clicked.connect(self.on_buy_clicked)
        self.__button_buy.setStyleSheet("QPushButton {border: none; background: green; color: white }"
                                        "QPushButton:pressed { background: black; }")
        self.__button_buy.setMinimumHeight(80)
        self.__button_buy.setFont(self.__button_back.font())
        self.__button_buy.hide()

    def on_qr_decoded(self, wallet):
        self.__label_enter_wallet.setText("Ваш кошелек:\n"+wallet)
        self.__widget_qr_scanner.hide()
        self.__button_buy.show()

    def on_back_clicked(self):
        print("e")
        self.on_close.emit(MainWindow.MainWindow())

    def on_buy_clicked(self):
        print(1)