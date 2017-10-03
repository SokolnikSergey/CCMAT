from CurrencySubscriber import CurrencySubscriber
class Subs(CurrencySubscriber):
    def __init__(self,publisher):

        self.__publisher = publisher
        self.__publisher.subscribe(self)

    def updated_uah_btc(self, new_uah_btc):
        super().updated_uah_btc(new_uah_btc)

    def updated_tax_for_owner(self, new_tax_for_owner):
        super().updated_tax_for_owner(new_tax_for_owner)

    def updated_tax_for_exchange(self, new_tax_for_exchange):
        super().updated_tax_for_exchange(new_tax_for_exchange)


