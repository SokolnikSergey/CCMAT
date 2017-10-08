from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject,QByteArray,pyqtSignal

from Client.SignalsBinder import SignalsBinder
from Client.InterrupConvertor import InterruptConvertor

import sys

class ClientBankomat(QObject):

    data_from_server_recieved = pyqtSignal(str) ##This signal is connected to the InterruptConvertor
                                                #that could detect what is the type of action


    def __init__(self,host = 'localhost',port=8080):

        super(ClientBankomat, self).__init__()
        self.__client = QTcpSocket()
        self.__client.connectToHost(host,port)


        self.snapping_signals()


    def snapping_signals(self):
        self.__client.readyRead.connect(self.read_data_from_server)

    def read_data_from_server(self):
        data = self.__client.readAll().data().decode("utf-8")
        self.data_from_server_recieved.emit(data)

    def write_data_to_server(self,str_data): ##This slot can be used at any case , when client want send data to server
        self.__client.write(QByteArray().append(str_data))

#
#
# app = QApplication([])
#
# c = ClientBankomat()
# i = InterruptConvertor()
#
# sys.exit(app.exec_())