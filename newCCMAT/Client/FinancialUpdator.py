import time
from threading import Thread

from Client.CurrencyOperations import CurrencyOperations


class FinancialUpdator(Thread):

    def __init__(self,polo= None,timer = 10,container_configurator =None , group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.__polo = polo
        self.__container_configurator = container_configurator
        self.__timer = timer

        self.do  = True




    def run(self):
        while(self.do):
            
            uah_dollar = CurrencyOperations.get_dol_uah()
            uah_btc =  uah_dollar * CurrencyOperations.get_btc_usd(self.__polo)
            transactions_fee =  CurrencyOperations.get_btc_transaction_fee(self.__polo)
            
            self.__container_configurator.currency_container_update_data(uah_btc,transactions_fee)
        
            time.sleep(self.__timer)