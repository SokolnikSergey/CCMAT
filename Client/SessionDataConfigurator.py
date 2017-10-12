from PyQt5.QtCore import QObject,pyqtSignal

class SessionDataConfigurator(QObject):
	
    monet_revieved_from_bill_acceptor = pyqtSignal(float)
	
    def __init__(self,session_data_container = None,currency_container = None):
        
        super(SessionDataConfigurator, self).__init__()
        self.__session_data_container = session_data_container
        self.__currency_container = currency_container

    def reciecer_address_decoded(self,address):
        if (isinstance(address,str)):
            self.__session_data_container.reciever_address = address

    def recieved_money_bill_acceptor(self,amout):
        print("Recieve money", amout)
        if amout and  isinstance(amout,(int,float)) and amout > 0:
            o_f =  self.__currency_container.owners_fee
            owners_fee = o_f if o_f < 1  else (o_f / 100)
            print(amout , owners_fee ,self.__currency_container.transactions_fee)
            self.monet_revieved_from_bill_acceptor.emit(amout  *  owners_fee * self.__currency_container.transactions_fee)
            # Send request to server for reservation amount_of_money
		    
			
    def inform_me(self,data):
        if data:
            self.__session_data_container.currency_for_operation = data.get("currency",None)
            self.__session_data_container.remaining_money_on_server = data.get("remain_money",-1)
            self.__currency_container.owners_fee = data.get("owners_fee",-1)


    def amount_kept(self,data):
        self.__session_data_container.remaining_money_on_server = data.get("amount_remained", -1)
        self.__session_data_container.recieved_money +=  data.get("amount_reserved", -1)
	
   
    def withdraw_complete(self,data):
        print("Withdraw complete")
        currency = data["currency"]
        amount = data["amount"]
        reciever_address = data["reciever"]
        #### print the reciept by this data
        self.__session_data_container.recieved_money = 0
	
        

    
