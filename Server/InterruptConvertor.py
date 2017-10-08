from PyQt5.QtCore import QObject,pyqtSignal
from ENUMS.ACTIONS import ACTIONS
from Server.Action import Action


class InterruptConvertor(QObject):

    response_has_made = pyqtSignal(object,dict)

    def __init__(self,action_queue  = None ):
        super(InterruptConvertor, self).__init__()
        self.__action_queue = action_queue



    def make_action(self,sock_sender,request_dict):
        action_type = request_dict["type"]
        if action_type not  in ACTIONS:
            action_type = None

        action_data = request_dict["data"]

        action = Action(action_type,action_data,sock_sender)
        self.__action_queue.add_action(action)


    def make_response(self,socket,data,response_errors,action_type):
            response = {"type":action_type,
                        "data":data,
                        "response_errors":response_errors}
            self.response_has_made.emit(response,socket)
            
