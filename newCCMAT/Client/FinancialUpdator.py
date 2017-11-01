import time
from threading import Thread
from requests.exceptions import ConnectionError
from PyQt5.QtCore import QObject,pyqtSignal


from Client.CurrencyOperations import CurrencyOperations


class FinancialUpdator(QObject,Thread):

    noInternetConnection = pyqtSignal()
    internetConnectionResumed = pyqtSignal()

    def __init__(self,polo= None,timer = 10,container_configurator =None , group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super(FinancialUpdator, self).__init__()
        #super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.__polo = polo
        self.__container_configurator = container_configurator
        self.__timer = timer

        self.do  = True

    def run(self):
        while(self.do):

            try:
                uah_dollar = CurrencyOperations.get_dol_uah()
                self.internetConnectionResumed.emit()
                uah_btc =  uah_dollar * CurrencyOperations.get_btc_usd(self.__polo)
                transactions_fee =  CurrencyOperations.get_btc_transaction_fee(self.__polo)
                self.__container_configurator.currency_container_update_data(uah_btc,transactions_fee)

            except ConnectionError:
                print("No Internet connection The default values has set")
                self.__container_configurator.currency_container_update_data(170150.12321321321, 0.001)

                self.noInternetConnection.emit()

            time.sleep(self.__timer)