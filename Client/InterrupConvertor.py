from PyQt5.QtCore import QObject,pyqtSignal
import json
from ENUMS.CURRENCIES import CURRENCIES
from ENUMS.ACTIONS import ACTIONS

class InterruptConvertor(QObject):

    inform_me = pyqtSignal(dict)
    actual_data  = pyqtSignal(dict)
    withdraw_complete = pyqtSignal(dict)
    request_has_made = pyqtSignal(str)
    
    

    def __init__(self):
        super(InterruptConvertor,self).__init__()

    def translate_data_from_server(self,data):
        return json.loads(data)

    def translate_data_to_server(self, data):
        return json.dumps(data)

    def detect_action(self,data_from_server):
        data = self.translate_data_from_server(data_from_server)

        action_type = data.get("type",None)

        if action_type:
            
            action_data = data.get("data", None)
            action_errors = data.get("response_errors",None)

            if not action_errors:
                
                if action_type == ACTIONS.InformMe:
                    self.inform_me.emit(action_data)

                elif action_type == ACTIONS.KeepAmountActualMoney:
                    self.actual_data.emit(action_data)

                elif action_type == ACTIONS.Withdraw:
                    self.withdraw_complete.emit(action_data)
                    
                    
    def make_inform_me_btc_request(self):
        request  = {
                        "type": ACTIONS.InformMe,
                        "data": {"currency": CURRENCIES.BitCoin}
                    }
        self.request_has_made.emit(self.translate_data_to_server(request))
	    
	def make_keep_amount_btc_money_to_reserve_request(self,money_to_reserve): ##This money sets with all fees
		request = {
		    "type": ACTIONS.KeepAmountActualMoney,
		    "data": {"currency": CURRENCIES.BitCoin,"amount_money_to_reserve": money_to_reserve}
	    }
		
		self.request_has_made.emit(self.translate_data_to_server(request))


	def make_withdraw_btc_request(self, amount,reciever_address):  ##This money sets with all fees
		request = {
			"type": ACTIONS.KeepAmountActualMoney,
			"data": {"currency": CURRENCIES.BitCoin,
			         "reciever": reciever_address,
			         'amount':amount}
		}
		self.request_has_made.emit(self.translate_data_to_server(request))

        







