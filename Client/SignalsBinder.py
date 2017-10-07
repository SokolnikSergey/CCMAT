from PyQt5.QtCore import QObject

class SignalsBinder(QObject):
    def __init__(self,client_bankomat,interrupt_convertor,session_data_configurator):
        super(SignalsBinder, self).__init__()

        self.__interrupt_convertor = interrupt_convertor
        self.__client_bankomat = client_bankomat
        self.__session_data_configurator = session_data_configurator

        self.snapping_client_bankomat_signals()
        self.snapping_signals_interrupt_convertor()

    def snapping_client_bankomat_signals(self):
        self.__client_bankomat.data_from_server_recieved.connect(self.__interrupt_convertor.detect_action)

    def snapping_signals_interrupt_convertor(self):
        self.__interrupt_convertor.inform_me.connect(self.__session_data_configurator.inform_me)