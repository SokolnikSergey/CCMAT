import poloniex

from PyQt5.QtWidgets import QApplication
import sys
from Client.ClientBankomat import ClientBankomat
from Client.CurrencyContainer import CurrencyContainer
from Client.FinancialUpdator import FinancialUpdator
from Client.InterrupConvertor import InterruptConvertor
from Client.SignalsBinder import SignalsBinder
from Client.SessionDataConfigurator import SessionDataConfigurator
from Client.SessionDataContainer import SessionDataContainer
from Client.Subs import Subs

class Starter:
	
	def __init__(self):
		self.create_poloniex_objects()
		self.create_aux_objects()
		self.start_working()
	
	def create_poloniex_objects(self):

		self.__public_polo = poloniex.PoloniexPublic()
	
	
	def create_aux_objects(self):
		self.__client_bankomat = ClientBankomat()
		self.__currency_container = CurrencyContainer()
		self.__finanсial_updator = FinancialUpdator(self.__public_polo,15,self.__currency_container)
		
		self.__interrupt_convertor = InterruptConvertor()
		
		self.__session_data_container  = SessionDataContainer()
		self.__session_data_configurator = SessionDataConfigurator(self.__session_data_container,self.__currency_container)
		
		self.__signals_binder = SignalsBinder(self.__client_bankomat,self.__interrupt_convertor,self.__session_data_configurator)
		
		
		
	def start_working(self):
		
		s = Subs(self.__currency_container)
		self.__finanсial_updator.start()
		self.__interrupt_convertor.make_inform_me_btc_request()
		#self.__session_data_configurator.recieved_money_bill_acceptor(20)
		#self.__interrupt_convertor.make_keep_amount_btc_money_to_reserve_request(20)
		#self.__interrupt_convertor.make_withdraw_btc_request(0.0,'a[sld[as[da[sd[asd')
		
	
app = QApplication([])

s = Starter()


sys.exit(app.exec_())