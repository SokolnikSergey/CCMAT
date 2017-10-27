import subprocess

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
from Client.QrController import QRController
from Client.CurrencyContainerConfigurator import CurrencyContainerConfigurator
from Client.AuxiliaryInformationContainer import AuxiliaryInformationContainer
from Client.InformationFiller import InformationFiller

from Client.ClientBillAcceptor import BillServer

from Client.MainViewController import MainViewController
from MainWindow import MainWindow


class Starter:
    def __init__(self):
        self.create_poloniex_objects()
        self.create_aux_objects()
        self.start_working()

    def create_poloniex_objects(self):
        self.__public_polo = poloniex.PoloniexPublic()

    def create_aux_objects(self):
        self.__aux_info_container = AuxiliaryInformationContainer()
        self.__aux_info_filler = InformationFiller(self.__aux_info_container)
        self.__aux_info_filler.fill_container_by_file_data()

        self.__client_bankomat = ClientBankomat(host='192.168.0.103')
        self.__currency_container = CurrencyContainer()

        self.__client_bill_validator = BillServer()

        self.__currency_container_configurator = CurrencyContainerConfigurator(self.__currency_container)

        self.__finanсial_updator = FinancialUpdator(self.__public_polo, 15, self.__currency_container_configurator)

        self.__session_data_container = SessionDataContainer()
        self.__session_data_configurator = SessionDataConfigurator(self.__session_data_container,
                                                                   self.__currency_container)
        self.__interrupt_convertor = InterruptConvertor(self.__aux_info_container, self.__currency_container,
                                                        self.__session_data_container)
        self.qr_controller = QRController()

        self.main_window_view = MainWindow(self.__session_data_configurator, self.__client_bill_validator)
        self.__main_window_controller = MainViewController(self.main_window_view, self.__currency_container)

        self.__signals_binder = SignalsBinder(self.__client_bankomat, self.__interrupt_convertor,
                                              self.__session_data_configurator,
                                              client_bill_validator=self.__client_bill_validator,
                                              view_operator=self.__main_window_controller,
                                              qr_decoder=self.qr_controller)
        print(55)
    def start_working(self):
        s = Subs(self.__currency_container)
        self.__finanсial_updator.start()


app = QApplication([])

s = Starter()
s.main_window_view.showFullScreen()

sys.exit(app.exec_())