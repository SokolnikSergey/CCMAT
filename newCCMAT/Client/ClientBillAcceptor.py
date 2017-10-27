from PyQt5.QtNetwork import QTcpServer, QHostAddress
from PyQt5.QtCore import QObject, QByteArray, pyqtSignal

import json


class BillServer(QObject):
    money_received = pyqtSignal(int)

    def __init__(self, port=7777):
        super(BillServer, self).__init__()
        self.__socket = QTcpServer()
        self.__socket.listen(QHostAddress.Any, port)

        self.__list_of_sockets = []

        self.snapping_signals()


    def snapping_signals(self):
        self.__socket.newConnection.connect(self.add_new_connection)

    def add_new_connection(self):
        sock = self.__socket.nextPendingConnection()
        sock.readyRead.connect(self.read_data_from_socket)

        if sock not in self.__list_of_sockets:
            self.__list_of_sockets.append(sock)

    def read_data_from_socket(self):
        sender = self.sender()
        data = sender.readAll().data().decode("utf-8")
        print("nom", data)
        self.money_received.emit(int(data)) ##transfer data to int <because it is amount of money>



