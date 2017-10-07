from PyQt5.QtCore import QObject,pyqtSignal
import json

from ENUMS.ACTIONS import ACTIONS

class InterruptConvertor(QObject):

    inform_me = pyqtSignal(dict)
    actual_data  = pyqtSignal(dict)
    withdraw = pyqtSignal(dict)

    def __init__(self):
        super(InterruptConvertor,self).__init__()

    def translate_data_from_server(self,data):
        return json.loads(data)

    def detect_action(self,data_from_server):
        data = self.translate_data_from_server(data_from_server)

        action_type = data.get("type",None)

        if action_type:
            action_data = data.get("data", None)

            if action_type == ACTIONS.InformMe:
                self.inform_me.emit(action_data)

            elif action_type == ACTIONS.KeepAmountActualMoney:
                self.actual_data.emit(action_data)

            elif action_type == ACTIONS.Withdraw:
                self.withdraw.emit(action_data)







