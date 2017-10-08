class SessionDataConfigurator:

    def __init__(self,session_data_container):
        self.__session_data_container = session_data_container

    def recieved_money(self,amout):
        if amout and  isinstance(amout,(int,float)) and amout > 0:
            self.__session_data_container.recieved_money +=  amout


    def keep_amount_actual_money_on_server(self,amount):
        self.__session_data_container.remaining_money_on_server = amount

    def inform_me(self,data):
        if data:
            self.__session_data_container.remaining_money_on_server = data.get("remian_money",-1)
            self.__session_data_container.owners_fee = data.get("owner_fee",-1)


    def amount_kept(self,data):
        pass

    def withdraw_complete(self,data):
        pass 


    
