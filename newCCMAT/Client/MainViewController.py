from PyQt5.QtCore import QObject,pyqtSignal
class MainViewController(QObject):

	inform_me_recieved = pyqtSignal()
	buy_recieved = pyqtSignal()
	bill_accepted = pyqtSignal(int)

	def __init__(self, main_view  = None,publisher = None):
		super(MainViewController, self).__init__()
		self.__main_view = main_view
		self.__publisher = publisher

		self.__main_view.inform_me.connect(self.inform_me_recieved)
		self.__main_view.buy_clicked.connect(self.buy_recieved)
		self.__main_view.bill_accepted.connect(self.bill_accepted)
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
