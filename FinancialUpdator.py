from threading import Thread
import time
from CurrencyOperations import CurrencyOperations

class FinancilacUpdator(Thread):

    def __init__(self,polo= None, container =None , group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.polo = polo
        self.container = container

        self.do  = True

    def run(self):
        while(self.do):
            self.container.uah_btc = CurrencyOperations.get_btc_usd(self.polo)
            time.sleep(10)