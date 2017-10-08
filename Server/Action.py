class Action:
    def __init__(self,operation_type = None,operation_data = None,socket_sender = None):

        self.__operation_type = operation_type
        self.__operation_data = operation_data
        self.__socket_sender = socket_sender


    @property
    def operation_type (self):
        return self.__operation_type

    @property
    def operation_data(self):
        return self.__operation_data

    @property
    def socket_sender (self):
        return self.__socket_sender


