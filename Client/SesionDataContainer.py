from ENUMS.CURRENCIES import CURRENCIES
from Interfaces.SessionDataPublisher import SessionDataPublisher

class SessionDataContainer(SessionDataPublisher):
    def __init__(self,remaining_money_on_server = -1,money_recieved = -1, owners_fee = -1,reciever_address = "", currency = CURRENCIES.BitCoin):
        self.__remaining_money_on_server = remaining_money_on_server
        self.__owners_fee = owners_fee
        self.__recieved_money = money_recieved
        self.__reciever_address = reciever_address
        self.__currency_for_operation = currency

        self.__subscribers = []

    @property
    def  remaining_money_on_server(self):
        return self.__remaining_money_on_server

    @remaining_money_on_server.setter
    def remaining_money_on_server(self,new_remain_money):
        if isinstance(new_remain_money,(int,float)):
            self.__remaining_money_on_server = new_remain_money

    @property
    def recieved_money(self):
        return self.__recieved_money

    @recieved_money.setter
    def recieved_money(self, new_recieved_money):
        if isinstance(new_recieved_money, (int, float) ):
            self.__recieved_money = new_recieved_money

    @property
    def owners_fee(self):
        return self.__owners_fee
    
    @owners_fee.setter
    def owners_fee(self, new_owners_fee):
        if isinstance(new_owners_fee, (int, float)):
            self.__owners_fee = new_owners_fee

    @property
    def reciever_address(self):
        return self.__reciever_address
    
    @reciever_address.setter
    def reciever_address(self, new_reciever_address):
        if isinstance(new_reciever_address, str):
            self.__reciever_address = new_reciever_address

    @property
    def currency_for_operation(self):
        return self.__currency_for_operation

    @currency_for_operation.setter
    def currency_for_operation(self, new_currency_for_operation):

        if isinstance(new_currency_for_operation, str):
            self.__currency_for_operation = CURRENCIES(new_currency_for_operation)

        elif isinstance(new_currency_for_operation,CURRENCIES):
            self.__currency_for_operation = new_currency_for_operation

    def reciever_address_updated(self):
        for subs in self.__subscribers:
            subs.reciever_address_update(self.__reciever_address)

    def owners_fee_updated(self):
        for subs in self.__subscribers:
            subs.owners_fee_update(self.__owners_fee)

    def currency_for_operation_updated(self):
        for subs in self.__subscribers:
            subs.currency_for_operation_update(self.__currency_for_operation)

    def remaining_money_on_server_updated(self):
        for subs in self.__subscribers:
            subs.remaining_money_on_server_update(self.__remaining_money_on_server)

    def recieved_money_updated(self):
        for subs in self.__subscribers:
            subs.recieved_money_update(self.__recieved_money)

    def subscribe(self, subscriber):
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber)

            subscriber.reciever_address_update(self.__reciever_address)
            subscriber.owners_fee_update(self.__owners_fee)
            subscriber.transactions_fee_update(self.__transactions_fee)
            subscriber.currency_for_operation_update(self.__currency_for_operation)
            subscriber.remaining_money_on_server_update(self.__remaining_money_on_server)
            subscriber.recieved_money_update(self.__recieved_money)

    def unsubscribe(self, subscriber):
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)








