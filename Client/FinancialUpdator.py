import time
from threading import Thread

from Client.CurrencyOperations import CurrencyOperations


class FinancialUpdator(Thread):

    def __init__(self,polo= None,timer = 10,container =None , group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.__polo = polo
        self.__container = container
        self.__timer = timer

        self.do  = True




    def run(self):
        while(self.do):
            
            uah_btc = CurrencyOperations.get_btc_usd(self.__polo)
            uah_dollar = CurrencyOperations.get_dol_uah()
            transactions_fee =  CurrencyOperations.get_btc_transaction_fee(self.__polo)

            self.__container.uah_btc = uah_btc
            self.__container.uah_dollar =uah_dollar
            self.__container.transactions_fee = transactions_fee

            time.sleep(self.__timer)