from PyQt5.QtCore import QObject,pyqtSignal
from ENUMS.CURRENCIES import CURRENCIES

class BalanceInformationConfigurator(QObject):

    amount_of_btc_kept = pyqtSignal(float,float)

    def __init__(self,balance_information_container = None):
        super(BalanceInformationConfigurator, self).__init__()
        self.__balance_information_container = balance_information_container

    def set_btc_balance(self,balance):
        print("set btc balance")
        self.__balance_information_container.btc_balance = balance

    def keep_amount_of_money(self,currency,amount_of_money_to_reserve):
        print(amount_of_money_to_reserve)
        if currency == CURRENCIES.BitCoin:
            if (self.__balance_information_container.btc_balance - amount_of_money_to_reserve > 0):
                
                self.__balance_information_container.btc_balance -=  amount_of_money_to_reserve
                self.__balance_information_container.btc_reserved += amount_of_money_to_reserve
                
                self.amount_of_btc_kept.emit(self.__balance_information_container.btc_balance,amount_of_money_to_reserve)
                return self.__balance_information_container.btc_balance
        return -1


    def take_into_account_btc_outflow(self,currency,amount):
        if currency == CURRENCIES.BitCoin:
            self.__balance_information_container.btc_balance -= amount
            self.__balance_information_container.btc_reserved -= amount
