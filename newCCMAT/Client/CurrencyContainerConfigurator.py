
class CurrencyContainerConfigurator:
	
	def __init__(self,currency_container = None):
		self.__currency_container = currency_container
		
	def currency_container_update_data(self,uah_btc,transactions_fee):
		self.__currency_container.uah_btc = uah_btc
		self.__currency_container.transactions_fee = transactions_fee
		
		