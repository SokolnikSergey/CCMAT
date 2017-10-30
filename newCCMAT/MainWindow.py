from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QFont, QIcon
from PyQt5.Qt import Qt, QSize, QTimer, QDateTime, QDate, QTime, pyqtSignal, QFontDatabase
from BuyCoinsWindow import BuyCoinsWindow
from Button import ImageButton
from InfoUI import InfoUI
from CryptoCurrenciesUI import CryptoCurrenciesUI

class MainWindow(QWidget):

    inform_me = pyqtSignal()
    buy_clicked = pyqtSignal()
    bill_accepted = pyqtSignal(int)

    def __init__(self, session_configurator, bills_server):
        super(MainWindow, self).__init__()
        self.create_widgets()
        self.prepare_layouts()
        self.config_widgets()

        self.__session_configurator = session_configurator
        self.__bills_server = bills_server
        print(1)

    def create_widgets(self):
        self.buy_coins_window = 0
        self.__help_window = 0
        self.__other_curr_window = 0
        self.__vlay_root = QVBoxLayout()
        self.__vlay_main = QVBoxLayout()
        self.__hlay_buttons_buy_coins = QHBoxLayout()

        self.__label_logo = QLabel("<img src=\"images/logo.png\">")
        self.__label_select_currency = QLabel("Купить")
        self.__label_time_date = QLabel()

        self.button_bitcoin = ImageButton("Bitcoin","images/bitcoin.png")
        self.__button_info = QPushButton("ПОМОЩЬ")
        self.__button_others_currency = QPushButton("ВСЕ КРИПТОВАЛЮТЫ")

        self.__effect_shadow1 = QGraphicsDropShadowEffect()

        self.__timer = QTimer()
        print(123)

    def prepare_layouts(self):

        self.__vlay_root.addWidget(self.__label_time_date)
        self.__vlay_root.addLayout(self.__vlay_main)

        self.__vlay_main.setAlignment(Qt.AlignCenter)
        self.__vlay_main.setSpacing(0)
        self.__vlay_main.addWidget(self.__label_logo)
        self.__vlay_main.addStretch(0)
        self.__vlay_main.addWidget(self.__label_select_currency)
        self.__vlay_main.addLayout(self.__hlay_buttons_buy_coins)
        self.__vlay_main.addStretch(0)
        self.__vlay_main.addSpacing(10)
        #self.__vlay_main.addWidget(self.__button_others_currency)
        self.__vlay_main.addWidget(self.__button_info)
        self.__vlay_main.setContentsMargins(0, 0, 0, 70)

        self.__hlay_buttons_buy_coins.addWidget(self.button_bitcoin)

        self.setLayout(self.__vlay_root)

    def config_widgets(self):

        id = QFontDatabase.addApplicationFont("fonts/Ubuntu-R.ttf")
        print("leen",len(QFontDatabase.applicationFontFamilies(id)[0]))
        ubuntu_font = QFont(QFontDatabase.applicationFontFamilies(id)[0], 22)

        self.button_bitcoin.setCurrency("")
        self.button_bitcoin.setFixedSize(250, 250)
        self.__button_others_currency.setStyleSheet("QPushButton { background: rgb(66, 101, 244); color: white; border-radius: 5px; }"
                                                    "QPushButton:pressed { background: black; }")
        self.__button_info.setIcon(QIcon("images/info.png"))
        self.__button_info.setIconSize(QSize(20, 20))

        self.__button_info.setStyleSheet("QPushButton { background: transparent; color: black; border-radius: 5px; }"
                                         "QPushButton:pressed { background: black; color: white }")

        self.__button_info.setMinimumHeight(50)
        self.__button_info.setFont(ubuntu_font)
        self.button_bitcoin.setFont(self.__button_info.font())
        self.__button_others_currency.setMinimumHeight(self.__button_info.minimumHeight())
        self.__button_others_currency.setFont(self.__button_info.font())
        self.__label_logo.setAlignment(Qt.AlignCenter)
        self.__label_select_currency.setFont(self.__button_info.font())
        self.__label_select_currency.setAlignment(Qt.AlignCenter)
        self.__label_select_currency.setMinimumHeight(30)

        self.button_bitcoin.clicked.connect(self.on_crypt_selected)

        self.__effect_shadow1.setBlurRadius(10)
        self.__effect_shadow1.setOffset(4)
        self.__button_others_currency.setGraphicsEffect(self.__effect_shadow1)

        self.__timer.timeout.connect(self.on_timer_timeout)
        self.__timer.start(1000)

        self.__label_time_date.setAlignment(Qt.AlignLeft)
        self.__label_time_date.setFont(ubuntu_font)

        self.__button_info.clicked.connect(self.on_button_help)

        self.__button_others_currency.clicked.connect(self.ob_button_other_curr)

    def on_crypt_selected(self):
        self.inform_me.emit()
        if(self.sender() == self.button_bitcoin):
            self.buy_coins_window = BuyCoinsWindow("BTC", self.__session_configurator, self.__bills_server)
        self.buy_coins_window.showFullScreen()

        self.buy_coins_window.buy_clicked.connect(self.buy_clicked)
        self.bill_accepted.connect(self.buy_coins_window.bill_accepted)

    def on_timer_timeout(self):
        self.update_time()

    def update_time(self):
        date_time = QDateTime().currentDateTime()
        date = date_time.date()
        time = date_time.time()
        self.__label_time_date.setText("{0}.{1}.{2}, {3}:{4}".format(date.day(), date.month(), date.year(), time.hour(), time.minute()))

    def on_button_help(self):
        self.__help_window = InfoUI()
        self.__help_window.showFullScreen()

    def ob_button_other_curr(self):
        self.__other_curr_window = CryptoCurrenciesUI()
        self.__other_curr_window.showFullScreen()