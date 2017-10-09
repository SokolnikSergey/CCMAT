class SessionDataConfigurator:

    def __init__(self,session_data_container):
        self.__session_data_container = session_data_container

    # def recieved_money(self,amout):
    #     if amout and  isinstance(amout,(int,float)) and amout > 0:
    #         self.__session_data_container.recieved_money +=  amout
    #
    #
    # def keep_amount_actual_money_on_server(self,amount):
    #     self.__session_data_container.remaining_money_on_server = amount

    def inform_me(self,data):
        if data:
            self.__session_data_container.currency_for_operation = data.get("currency",None)
            self.__session_data_container.remaining_money_on_server = data.get("remian_money",-1)
            self.__session_data_container.owners_fee = data.get("owners_fee",-1)


    def amount_kept(self,data):
        self.__session_data_container.remaining_money_on_server = data.get("amount_remained", -1)
        self.__session_data_container.recieved_money +=  data.get("amount_reserved", -1)
   
    def withdraw_complete(self,data):
        currency =  data["currency"]
        amount =  data["amount"]
        reciever_address = data["reciever"]


    
