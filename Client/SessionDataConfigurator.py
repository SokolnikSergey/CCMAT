class SessionDataConfigurator:

    def __init__(self,session_data_container = None,currency_container = None):
        self.__session_data_container = session_data_container
        self.__currency_container = currency_container

    def recieved_money_bill_acceptor(self,amout):
        if amout and  isinstance(amout,(int,float)) and amout > 0:
            o_f =  self.__currency_container.owners_fee
            owners_fee = o_f if o_f < 1 else (o_f / 100)
            self.__session_data_container.recieved_money += amout  *  owners_fee * self.__currency_container.transactions_fee

    def inform_me(self,data):
        if data:
            self.__session_data_container.currency_for_operation = data.get("currency",None)
            self.__session_data_container.remaining_money_on_server = data.get("remain_money",-1)
            self.__currency_container.owners_fee = data.get("owners_fee",-1)


    def amount_kept(self,data):
        self.__session_data_container.remaining_money_on_server = data.get("amount_remained", -1)
        self.__session_data_container.recieved_money +=  data.get("amount_reserved", -1)
	
   
    def withdraw_complete(self,data):
        currency = data["currency"]
        amount = data["amount"]
        reciever_address = data["reciever"]
        
        self.__session_data_container.recieved_money = 0
	
        

    
