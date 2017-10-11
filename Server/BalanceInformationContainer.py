class BalanceInformationContainer:
    
    def __init__(self,btc_balance = 100,btc_reserved = 0 ):
        self.__btc_balance = btc_balance
        self.__btc_reserved = btc_reserved
        
    @property
    def btc_balance(self):
        return self.__btc_balance
    
    @btc_balance.setter
    def btc_balance(self,new_btc_balance):
        if (new_btc_balance and isinstance(new_btc_balance,(int,float))):
            self.__btc_balance = new_btc_balance

    @property
    def btc_reserved(self):
        return self.__btc_reserved

    @btc_reserved.setter
    def btc_reserved(self, new_btc_reserved):
        if (new_btc_reserved and isinstance(new_btc_reserved, (int, float))):
            self.__btc_reserved = new_btc_reserved

