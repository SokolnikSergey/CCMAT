class BalanceUpdator:
    def __init__(self,balance_information_configurator = None):
        self.__balance_info_configurator = balance_information_configurator


    def update_btc_balance(self):
        balance = 11 ##### There is should be request to API about balance
        self.__balance_info_configurator.set_btc_balance(balance)