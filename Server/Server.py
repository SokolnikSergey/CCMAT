from PyQt5.QtNetwork import QTcpServer,QHostAddress
from PyQt5.QtCore import QObject,QByteArray,pyqtSignal
from PyQt5.QtWidgets import QApplication

import json

import sys


class Server(QObject):

    data_recieved = pyqtSignal(object,str)

    def __init__(self):
        super(Server, self).__init__()
        self.__socket = QTcpServer()
        self.__socket.listen(QHostAddress.Any,8080)

        self.__list_of_sockets = []

        self.snapping_signals()

    def terminate_connection_with_bankomat(self,socket):
        pass

    def snapping_signals(self):
        self.__socket.newConnection.connect(self.add_new_connection)


    def add_new_connection(self):

        sock  = self.__socket.nextPendingConnection()
        sock.readyRead.connect(self.read_data_from_socket)

        if sock not in self.__list_of_sockets:
            self.__list_of_sockets.append(sock)


    def read_data_from_socket(self):
        sender = self.sender()
        data = sender.readAll().data().decode("utf-8")
        self.data_recieved.emit(sender,data)


    def write_data_to_socket(self,dict_data,response_reciever):
        response_reciever.write(QByteArray().append(json.dumps(dict_data)))
        self.terminate_connection_with_bankomat(response_reciever)
        


app = QApplication([])

s = Server()

sys.exit(app.exec_())