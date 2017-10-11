
from Server.AuxiliaryInformationContainer import AuxiliaryInformationContainer
from Server.BalanceInformationContainer import BalanceInformationContainer
from Server.BalanceInformationConfigurator import BalanceInformationConfigurator
from Server.InterruptConvertor import InterruptConvertor
from Server.ActionQueue import ActionQueue
from Server.ActionPerformer import ActionPerformer
from Server.OperationExecutor import OperationExecutor
from Server.SignalsBinder import SignalsBinder
from Server.ServerMain import Server
from Server.InformationFiller import InformationFiller
from PyQt5.QtWidgets import QApplication

import sys


class Starter:
	
	def __init__(self):
		self.create_aux_objects()
		self.start_actions()
	
	def create_aux_objects(self):
		
		self.__server = Server()
		
		self.__aux_info_container = AuxiliaryInformationContainer()
		
		self.__information_filler  = InformationFiller(self.__aux_info_container)
		
		self.__balance_information_container = BalanceInformationContainer()
		self.__balance_information_configurator = BalanceInformationConfigurator(self.__balance_information_container)
		
		self.__action_queue = ActionQueue()
		
		self.__interrupt_convertor = InterruptConvertor(self.__action_queue)
		
		self.__operation_executor = OperationExecutor("TYMLRP8Z-SG0T22XB-5IF7VU4M-U6G37O0R",
			"f8844f0c5064fc3786ea20906faa20fd79259ba24b718f4615b6057162678c09171edc61ea4eaeb7fec73cbf918343dc2c7b43028968783b5900fd0e987b102c",
		                self.__aux_info_container)
		
		self.__action_performer = ActionPerformer(self.__action_queue,self.__operation_executor,self.__balance_information_configurator)
		
		self.__signals_binder =  SignalsBinder(self.__server,self.__interrupt_convertor,
		                            self.__balance_information_configurator,self.__action_queue,self.__action_performer)
	
	
	def start_actions(self):
		self.__information_filler.fill_container_by_file_data()
	
		
app = QApplication([])

s = Starter()

sys.exit(app.exec_())