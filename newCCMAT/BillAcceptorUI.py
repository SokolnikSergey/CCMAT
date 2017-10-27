from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt, pyqtSignal


class BillAcceptorUI(QWidget):

    bill_accepted = pyqtSignal(int)

    def __init__(self, bills_server):
        super(BillAcceptorUI, self).__init__()
        self.bills = 0
        self.bills_server = bills_server
        self.createObjects()
        self.configObjects()



    def createObjects(self):
        self.__vlay_main = QVBoxLayout()

        self.__label_enter_money = QLabel("Вставьте купюру<br><br><img src=\"images/cash.png\">")

        self.__button_add10 = QPushButton("10")
        self.__button_add50 = QPushButton("50")
        self.__button_add100 = QPushButton("100")


    def configObjects(self):

        self.setLayout(self.__vlay_main)

        self.__vlay_main.setSpacing(0)
        self.__vlay_main.addWidget(self.__label_enter_money)
        self.__vlay_main.addWidget(self.__button_add10)
        self.__vlay_main.addWidget(self.__button_add50)
        self.__vlay_main.addWidget(self.__button_add100)
        self.__vlay_main.setContentsMargins(0, 0, 0, 0)

        self.__label_enter_money.setFont(QFont("Segoe UI", 15))
        self.__label_enter_money.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("background: rgb(66, 101, 244); color: white;")

        self.__button_add10.setStyleSheet("QPushButton { background: rgb(66, 111, 255); color: white; border: none }"
                                          "QPushButton:pressed { background: black; }")
        self.__button_add10.setFixedHeight(50)

        self.__button_add50.setStyleSheet(self.__button_add10.styleSheet())
        self.__button_add50.setFixedHeight(self.__button_add10.height())
        self.__button_add100.setStyleSheet(self.__button_add10.styleSheet())
        self.__button_add100.setFixedHeight(self.__button_add10.height())

        self.__button_add10.clicked.connect(self.on_buttons_add)
        self.__button_add50.clicked.connect(self.on_buttons_add)
        self.__button_add100.clicked.connect(self.on_buttons_add)

        self.__button_add10.hide()
        self.__button_add50.hide()
        self.__button_add100.hide()

        self.bills_server.money_received.connect(self.on_bill_accepted)


    def on_bill_accepted(self, bill_denomination):
        self.bills += bill_denomination
        self.bill_accepted.emit(bill_denomination)
        self.update_info()

    def update_info(self):
        self.__label_enter_money.setText("Внесена сумма:<br><br>"+str(self.bills)+"<br><br><img src=\"images/cash.png\">")

    def on_buttons_add(self):
        if(self.sender() == self.__button_add10):
            self.on_bill_accepted(10)
        elif(self.sender() == self.__button_add50):
            self.on_bill_accepted(50)
        elif(self.sender() == self.__button_add100):
            self.on_bill_accepted(100)

    def printTicket(self):
        self.__label_enter_money.setText("Заберите чек!<br><br><img src=\"images/ticket.png\">")
