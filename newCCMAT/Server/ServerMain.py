from PyQt5.QtNetwork import QTcpServer, QHostAddress
from PyQt5.QtCore import QObject, QByteArray, pyqtSignal

import json


class Server(QObject):
    data_recieved = pyqtSignal(object, str)

    def __init__(self, port=8080):
        super(Server, self).__init__()
        self.__socket = QTcpServer()
        self.__socket.listen(QHostAddress.Any, port)

        self.__list_of_sockets = []

        self.snapping_signals()

    def terminate_connection_with_bankomat(self, socket):
        pass

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

        self.data_recieved.emit(sender, data)

    def write_data_to_socket(self, response_reciever, dict_data):
        response_reciever.write(QByteArray().append(json.dumps(dict_data)))
        self.terminate_connection_with_bankomat(response_reciever)





#
# connector = DataBaseConnector(database="bankomat")
# conn = connector.get_connector(connector.config)
# transactor = DataBaseTransactor(conn)
# transactor.result_of_withdraw("1", "2", "imei_bankomat123", "BEL Minsk", "BTC", 1.111111, 0.366)