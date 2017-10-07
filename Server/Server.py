from PyQt5.QtNetwork import QTcpServer,QHostAddress
from PyQt5.QtCore import QObject,QByteArray
from PyQt5.QtWidgets import QApplication

import json

import sys


class Server(QObject):

    def __init__(self):
        super(Server, self).__init__()
        self.__socket = QTcpServer()
        self.__socket.listen(QHostAddress.Any,8080)

        self.__list_of_sockets = []

        self.snapping_signals()

    def snapping_signals(self):
        self.__socket.newConnection.connect(self.add_new_connection)


    def add_new_connection(self):

        sock  = self.__socket.nextPendingConnection()
        sock.readyRead.connect(self.read_data_from_socket)

        if sock not in self.__list_of_sockets:
            self.__list_of_sockets.append(sock)


    def read_data_from_socket(self):
        print(self.sender().readAll())
        self.write_data_to_socket()


    def write_data_to_socket(self):
        self.sender().write(QByteArray().append(json.dumps({"action":"Hello from server action"})))


app = QApplication([])

s = Server()

sys.exit(app.exec_())