from PyQt5.QtCore import QObject,pyqtSignal
from ENUMS.ACTIONS import ACTIONS
from ENUMS.CURRENCIES import CURRENCIES
from Server.Action import Action
import json


class InterruptConvertor(QObject):

    response_has_made = pyqtSignal(object,dict)

    def __init__(self,action_queue  = None ):
        super(InterruptConvertor, self).__init__()
        self.__action_queue = action_queue

    
    def translate_int_action_to_enum_action(self,value):
        return ACTIONS(value)
    
    def transtart_str_currency_to_enum_currenct(self,value):
        return CURRENCIES(value)

    def translate_enum_action_to_int(self, value):
        return value.value

    def transtart_enum_currenct_to_str_(self, value):
        return value.value

    def make_action(self,sock_sender,request_dict):
        request_dict =  json.loads(request_dict)
        
        action_type = self.translate_int_action_to_enum_action(request_dict["type"])
        
        action_data = request_dict["data"]
        
        action_data["currency"] = self.transtart_str_currency_to_enum_currenct(action_data["currency"])
        action = Action(action_type,action_data,sock_sender)
        self.__action_queue.add_action(action)


    def make_response(self,socket,data,response_errors,action_type):
        
            data["currency"] = self.transtart_enum_currenct_to_str_(data["currency"])
            action_type = self.translate_enum_action_to_int(action_type)
            response = {"type":action_type,
                        "data":data,
                        "response_errors":response_errors}
            self.response_has_made.emit(socket,response)
            
