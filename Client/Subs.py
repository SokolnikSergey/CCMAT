from Interfaces.CurrencySubscriber import CurrencySubscriber

class Subs(CurrencySubscriber):
    def __init__(self,publisher):

        self.__publisher = publisher

        self.subscribe()

    def updated_uah_btc(self, new_uah_btc):
        print("UAH_BTC->",new_uah_btc)

    def updated_uah_dollar(self,new_uah_dollar):
        print("UAH_DOLLAR->",new_uah_dollar)

    def transactions_fee_update(self, new_transactions_fee):
        print("BTC Transaction fee -> ", new_transactions_fee)

    def owners_fee_update(self, new_owners_fee):
        print("OWNER's fee updated->",new_owners_fee)
        
    def subscribe(self):
        self.__publisher.subscribe(self)
        
    def unsubscribe(self):
        self.__publisher.unsubscribe(self)
    

