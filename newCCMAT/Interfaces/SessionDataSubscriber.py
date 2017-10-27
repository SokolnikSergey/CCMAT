class SessionDataSubscriber:
    
    publisher = None

    def remaining_money_on_server_update(self,new_ramain_money):
        pass

    def transactions_fee_update(self,new_transactions_fee):
        pass

    def recieved_money_update(self,new_recieved_money):
        pass

    def reciever_address_update(self,new_reciever_address):
        pass

    def currency_for_operation_update(self,new_currency_for_operation):
        pass

    def subscribe(self,publisher):
        pass

    def unsubscribe(self,publisher):
        pass