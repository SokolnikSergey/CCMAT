
from Interfaces.CurrencyPublisher import CurrencyPublisher
class CurrencyContainer(CurrencyPublisher):
    def __init__(self,uah_btc = -1,uah_dollar = -1,transactions_fee = -1, owners_fee = -1 ):
        self.__uah_btc = uah_btc
        self.__uah_dollar = uah_dollar
        self.__transactions_fee = transactions_fee
        self.__owners_fee = owners_fee

        self.__subscribers = []

    @property
    def uah_btc(self):
        return self.__uah_btc

    @uah_btc.setter
    def uah_btc(self,new_uah_btc):
        if new_uah_btc and isinstance(new_uah_btc,(int,float)):
            self.__uah_btc = new_uah_btc
            self.update_uah_btc()


    @property
    def uah_dollar(self):
        return self.__uah_dollar

    @uah_dollar.setter
    def uah_dollar(self, new_uah_dollar):
        if new_uah_dollar and  isinstance(new_uah_dollar,(int,float)) :
            self.__uah_dollar = new_uah_dollar
            self.update_uah_dollar()
            

    @property
    def transactions_fee(self):
        return self.__transactions_fee

    @transactions_fee.setter
    def transactions_fee(self, new_transactions_fee):
        if new_transactions_fee and  isinstance(new_transactions_fee,(int,float)):
            self.__transactions_fee = new_transactions_fee
            self.transactions_fee_updated()

    @property
    def owners_fee(self):
        return self.__owners_fee

    @owners_fee.setter
    def owners_fee(self, new_owners_fee):
        if new_owners_fee and  isinstance(new_owners_fee,(int,float)):
            self.__owners_fee = new_owners_fee
            self.owners_fee_updated()
    
    def update_all(self):
        if self.__subscribers:
            for subscriber in self.__subscribers:
                subscriber.updated_uah_btc(self.__uah_btc)
                subscriber.updated_uah_dollar(self.__uah_dollar)
                subscriber.transactions_fee_update(self.__transactions_fee)
                subscriber.owners_fee_update(self.__owners_fee)

    def subscribe(self,subscriber):
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber)
            self.update_all()

    def unsubscribe(self,subscriber):
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)

    def update_uah_btc(self):
        if self.__subscribers:
            for subscriber in self.__subscribers:
                subscriber.updated_uah_btc(self.__uah_btc)

    def update_uah_dollar(self):
        if self.__subscribers:
            for subscriber in self.__subscribers:
                subscriber.updated_uah_dollar(self.__uah_dollar)


    def transactions_fee_updated(self):
        for subs in self.__subscribers:
            subs.transactions_fee_update(self.__transactions_fee)

    def owners_fee_updated(self):
        for subs in self.__subscribers:
            subs.owners_fee_update(self.__owners_fee)


    
