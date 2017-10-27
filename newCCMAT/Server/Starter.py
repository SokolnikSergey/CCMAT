
from Server.AuxiliaryInformationContainer import AuxiliaryInformationContainer
from Server.BalanceInformationContainer import BalanceInformationContainer
from Server.BalanceInformationConfigurator import BalanceInformationConfigurator
from Server.InterruptConvertor import InterruptConvertor
from Server.ActionQueue import ActionQueue
from Server.ActionPerformer import ActionPerformer
from Server.OperationExecutor import OperationExecutor
from Server.SignalsBinder import SignalsBinder
from Server.ServerMain import Server
from Server.DataBaseConnector import DataBaseConnector
from Server.DataBaseTransactor import DataBaseTransactor
from Server.InformationFiller import InformationFiller
from PyQt5.QtWidgets import QApplication

import sys


class Starter:
	
	def __init__(self):
		self.create_aux_objects()
	
	def create_aux_objects(self):
		
		self.__server = Server()
		
		self.__aux_info_container = AuxiliaryInformationContainer()
		
		self.__information_filler  = InformationFiller(self.__aux_info_container)
		self.__information_filler.fill_container_by_file_data()
		
		self.__balance_information_container = BalanceInformationContainer()
		self.__balance_information_configurator = BalanceInformationConfigurator(self.__balance_information_container)
		
		self.__action_queue = ActionQueue()
		
		self.__interrupt_convertor = InterruptConvertor(self.__action_queue)
		
		self.__operation_executor = OperationExecutor(self.__aux_info_container.api_key
		                        ,self.__aux_info_container.secret_key,self.__aux_info_container,self.__balance_information_container)
		
		self.__action_performer = ActionPerformer(self.__action_queue,self.__operation_executor,
		                                          self.__balance_information_configurator,self.__aux_info_container)
		
		self.__db_connector = DataBaseConnector(database="Bankomat")
		self.__db_transactor = DataBaseTransactor(self.__db_connector)
		
		self.__signals_binder =  SignalsBinder(self.__server,self.__interrupt_convertor,
		        self.__balance_information_configurator,self.__action_queue,self.__action_performer,self.__db_transactor)
	
	
		
	
		
app = QApplication([])

s = Starter()

sys.exit(app.exec_())