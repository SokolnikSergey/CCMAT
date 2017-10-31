from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.Qt import Qt, QTimer, pyqtSignal
from BillAcceptorUI import BillAcceptorUI
from QRScannerUI import QRScannerUI
import TEXT_CONSTANTS
from WarningUI import WarningUI

class BuyCoinsWindow(QWidget):

    bill_accepted = pyqtSignal(int)
    buy_clicked = pyqtSignal()

    def __init__(self, crypto_currency, session_configurator, bills_server):
        super(BuyCoinsWindow, self).__init__()
        self.__crypto_currency = crypto_currency
        print(1)
        self.__bills_server = bills_server
        print(bills_server)
        print(3)
        self.createObjects()
        self.prepareLayouts()
        print(2)
        print(3)
        self.configObjects()
        print(4)
        self.__wallet = ""
        self.__timeout = 16
        self.__session_configurator = session_configurator

        print(321)

    def createObjects(self):

        self.__hlay_main = QHBoxLayout()
        self.__vlay_left = QVBoxLayout()

        self.__widget_bill_acceptor = BillAcceptorUI(self.__bills_server)
        self.__widget_qr_scanner = QRScannerUI()

        self.__label_enter_wallet = QLabel(TEXT_CONSTANTS.BUY_COINS_WINDOW_QR_SCANNING)
        self.__label_logo = QLabel("<img src=\"images/logo.png\">")

        self.__button_buy = QPushButton(TEXT_CONSTANTS.BUY_COINS_WINDOW_NEXT_BUTTON)
        self.__button_back = QPushButton(TEXT_CONSTANTS.BUY_COINS_WINDOW_BACK_BUTTON)

        self.__timer = QTimer()

        self.__warning_window = WarningUI()


    def prepareLayouts(self):
        print("xxx")
        self.__hlay_main.setSpacing(0)
        print(00)
        self.__hlay_main.addLayout(self.__vlay_left)
        self.__hlay_main.addWidget(self.__widget_bill_acceptor)
        self.__hlay_main.setContentsMargins(0, 0, 0, 0)
        print(444)
        self.__vlay_left.addWidget(self.__button_back)
        self.__vlay_left.addWidget(self.__label_logo)
        self.__vlay_left.addWidget(self.__label_enter_wallet)
        self.__vlay_left.addWidget(self.__widget_qr_scanner)
        self.__vlay_left.addWidget(self.__button_buy)
        self.__vlay_left.setContentsMargins(0, 0, 0, 0)
        print(5555)
        self.setLayout(self.__hlay_main)

    def configObjects(self):

        id = QFontDatabase.addApplicationFont("fonts/Ubuntu-R.ttf")
        print("leen", len(QFontDatabase.applicationFontFamilies(id)[0]))
        ubuntu_font = QFont(QFontDatabase.applicationFontFamilies(id)[0], 15)

        self.__label_enter_wallet.setFont(ubuntu_font)
        self.__label_enter_wallet.setAlignment(Qt.AlignCenter)
        self.__label_enter_wallet.setWordWrap(True)

        self.__widget_qr_scanner.qr_decoded.connect(self.on_qr_decoded)

        self.__button_back.setFixedWidth(100)
        self.__button_back.setStyleSheet("QPushButton { color: black; border: none; }"
                                         "QPushButton:pressed { background: black; color: white; }")
        self.__button_back.setMinimumHeight(50)
        self.__button_back.setFont(ubuntu_font)
        self.__button_back.clicked.connect(self.on_back_clicked)

        self.__button_buy.clicked.connect(self.on_buy_clicked)
        self.__button_buy.setStyleSheet("QPushButton {border: none; background: green; color: white }"
                                        "QPushButton:pressed { background: black; }")
        self.__button_buy.setMinimumHeight(80)
        self.__button_buy.setFont(self.__button_back.font())
        self.__button_buy.hide()

        self.__widget_qr_scanner.qr_decoded.connect(self.on_qr_decoded)
        self.__widget_bill_acceptor.bill_accepted.connect(self.on_bill_accepted)
        self.__label_enter_wallet.setWordWrap(True)
        self.__label_logo.setAlignment(Qt.AlignCenter)

        self.__timer.timeout.connect(self.on_timer_timeout)

        self.__widget_bill_acceptor.hide()
        self.__warning_window.on_timeout.connect(self.on_timeout_warning)
        self.__warning_window.setLogo("<img src=\"images/logo.png\">")
        self.__warning_window.setText("BlaBlaBla")
        self.__warning_window.on_ok.connect(self.on_ok_warning)
        self.__warning_window.on_cancel.connect(self.on_cancel_warning)

    def on_qr_decoded(self, wallet):

        self.__wallet = self.prepareWalletAddress(wallet)
        print(self.__wallet)
        self.__session_configurator.reciecer_address_decoded(self.__wallet)
        self.__wallet = self.prepareWallet(self.__wallet)
        self.__label_enter_wallet.setText("Ваш колек:\n\n"+self.__wallet+TEXT_CONSTANTS.BUY_COINS_WINDOW_TIP1)
        print("eeerr")
        self.__widget_qr_scanner.hide()
        self.__session_configurator.monet_revieved_from_bill_acceptor.connect(self.on_money_keeped)
        self.__button_buy.show()

    def on_back_clicked(self):
        if(self.__widget_bill_acceptor.bills > 0):
            self.__warning_window.setText(TEXT_CONSTANTS.WARNING_WINDOW_TEXT2)
            self.__warning_window.showFullScreen()
        else:
            self.__widget_qr_scanner.stopCamera()
            self.deleteLater()


    def on_buy_clicked(self):
        if(self.__button_buy.text() == TEXT_CONSTANTS.BUY_COINS_WINDOW_BUY_BUTTON):
            self.__label_enter_wallet.setText(TEXT_CONSTANTS.BUY_COINS_WINDOW_TRANSACTION_SUCCESS)
            self.__timer.start(1000)
            self.__button_buy.hide()
            self.__widget_bill_acceptor.printTicket()
            self.buy_clicked.emit()
            self.__widget_bill_acceptor.bills = 0
            self.__warning_window.stopTimer()
        elif(self.__button_buy.text() == TEXT_CONSTANTS.BUY_COINS_WINDOW_NEXT_BUTTON):
            self.__widget_bill_acceptor.show()
            self.__button_buy.hide()
            self.__button_buy.setText(TEXT_CONSTANTS.BUY_COINS_WINDOW_BUY_BUTTON)
            self.__label_enter_wallet.setText("Ваш кошелек:\n\n"+self.__wallet)

    def on_bill_accepted(self, bills):
        print("12312qq")
        self.__warning_window.startTimer(60000)
        self.bill_accepted.emit(bills)
        self.show_buy_button()

    def show_buy_button(self):
        if(self.__widget_qr_scanner.isHidden() and self.__widget_bill_acceptor.bills > 0):
            self.__button_buy.show()
            print("111111")
            self.calculate_crypto_coins()
        elif(self.__widget_qr_scanner.isHidden() and self.__widget_bill_acceptor.bills == 0):
            self.__label_enter_wallet.setText("Ваш кошелек:\n\n"+self.__wallet)

    def calculate_crypto_coins(self):
        self.__session_configurator.recieved_money_bill_acceptor(self.__widget_bill_acceptor.bills)

    def on_timer_timeout(self):
        self.__button_back.setFixedWidth(140)
        if(self.__timeout > 1):
            self.__timeout -= 1
            self.__button_back.setText(TEXT_CONSTANTS.BUY_COINS_WINDOW_BACK_BUTTON+" ("+str(self.__timeout)+")")
        else:
            self.deleteLater()

    def on_money_keeped(self, coins):
        self.__label_enter_wallet.setText(
            "Ваш кошелек:\n" + self.__wallet + "\n\nБудет переведено: " + str(coins) +" " + self.__crypto_currency)

    def prepareWallet(self, wallet):
        count = 20
        new_wallet = ""
        for i in range(len(wallet)):
            count -= 1
            if(count != 0):
                new_wallet += wallet[i]
            else:
                new_wallet += wallet[i]+'\n'
                count = 20
        print(new_wallet)
        return new_wallet

    def prepareWalletAddress(self, wallet):
        print(12312312321)
        if "?" in wallet:
            pos = wallet.index("?")
            wallet = wallet[:pos]

        if ":" in wallet:
            pos = wallet.index(":")
            wallet = wallet[pos+1:]

        return wallet

    def on_timeout_warning(self):
        self.__warning_window.showFullScreen()

    def on_ok_warning(self):
        if(self.__warning_window.getText() == TEXT_CONSTANTS.WARNING_WINDOW_TEXT1):
            self.__warning_window.hide()
            self.__warning_window.startTimer(60000)
        elif(self.__warning_window.getText() == TEXT_CONSTANTS.WARNING_WINDOW_TEXT2):
            self.__widget_qr_scanner.stopCamera()
            self.deleteLater()
            self.__warning_window.deleteLater()

    def on_cancel_warning(self):
        if(self.__warning_window.getText() == TEXT_CONSTANTS.WARNING_WINDOW_TEXT2):
            self.__warning_window.hide()
        elif(self.__warning_window.getText() == TEXT_CONSTANTS.WARNING_WINDOW_TEXT1):
            self.__widget_qr_scanner.stopCamera()
            self.deleteLater()
            self.__warning_window.deleteLater()