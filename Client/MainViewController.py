class MainViewController:
	def __init__(self, main_view  = None,publisher = None):
		self.__main_view = main_view
		self.__publisher = publisher
	
		self.subsbribe()
		
	def subsbribe(self):
		self.__publisher.subscribe(self)
		
	def updated_uah_btc(self,new_uah_btc):
		self.__main_view.button_bitcoin.setCurrency(str(new_uah_btc))
	
	def updated_uah_dollar(self,uah_dollar):
		pass
	def transactions_fee_update(self,transactions_fee):
		pass
	def owners_fee_update(self,owners_fee):
		pass
