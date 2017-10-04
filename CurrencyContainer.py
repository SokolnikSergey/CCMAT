
from CurrencyPublisher import CurrencyPublisher
class CurrencyContainer(CurrencyPublisher):
    def __init__(self,uah_btc = None,tax_for_exchange = None,tax_for_owner = None):
        self.__uah_btc = uah_btc
        self.__tax_for_exchange = tax_for_exchange
        self.__tax_for_owner = tax_for_owner

        self.__subscribers = []

    @property
    def uah_btc(self):
        return self.__uah_btc

    @uah_btc.setter
    def uah_btc(self,new_uah_btc):
        if new_uah_btc:
            self.__uah_btc = new_uah_btc
            self.update_uah_btc()

    @property
    def tax_for_exchange(self):
        return self.__tax_for_exchange

    @tax_for_exchange.setter
    def tax_for_exchange(self, new_tax_for_exchange):
        if new_tax_for_exchange:
            self.__uah_btc = new_tax_for_exchange
            self.update_tax_for_exchange()

    @property
    def tax_for_owner(self):
        return self.__tax_for_owner

    @tax_for_owner.setter
    def tax_for_owner(self, new_tax_for_owner):
        if new_tax_for_owner:
            self.__uah_btc = new_tax_for_owner
            self.update_tax_for_owner()

    def update_tax_for_owner(self):
        if self.__subscribers:
            for subscriber in self.__subscribers:
                subscriber.updated_tax_for_owner(self.__tax_for_owner)

    def update_tax_for_exchange(self):
        if self.__subscribers:
            for subscriber in self.__subscribers:
                subscriber.updated_tax_for_exchange(self.__tax_for_exchange)

    def update_uah_btc(self):
        if self.__subscribers:
            for subscriber in self.__subscribers:
                subscriber.updated_uah_btc(self.__uah_btc)

    def update_all(self):
        if self.__subscribers:
            for subscriber in self.__subscribers:
                subscriber.updated_uah_btc(self.__uah_btc)
                subscriber.updated_tax_for_exchange(self.__tax_for_exchange)
                subscriber.updated_tax_for_owner(self.__tax_for_owner)


    def subscribe(self,subscriber):
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber)
            self.update_all()


    def unsubscribe(self,subscriber):
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)
