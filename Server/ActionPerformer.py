from PyQt5.QtCore import  QObject,pyqtSignal
from ENUMS.ACTIONS import ACTIONS

class ActionPerformer(QObject):

    action_done = pyqtSignal(object,dict,list,object)

    def __init__(self,action_queue = None,operations_executor = None,balance_info_configurator = None):
        super(ActionPerformer, self).__init__()
        self.__action_queue = action_queue
        self.__operations_executor = operations_executor
        self.__balance_inforation_configurator = balance_info_configurator


    def start_executing(self):
        while(self.__action_queue.size()):
            action = self.__action_queue.get_action()

            action_type = action.operation_type
            data  =  action.operation_data
            sender = action.socket_sender
        
            if action_type ==  ACTIONS.InformMe:
                response = self.__operations_executor.inform_me(data["currency"])
                self.__balance_inforation_configurator.set_btc_balance(response["data"]['remain_money'])
                self.action_done.emit(sender,response["data"], response["response_errors"],action_type)
                
              
            elif action_type == ACTIONS.KeepAmountActualMoney:
                balance = self.__balance_inforation_configurator.keep_amount_of_money(data["currency"],data["amount_money_to_reserve"])
                
                if ( balance != -1 ) :
                    response = {"currency": data["currency"],
                                "amount_reserved": data["amount_money_to_reserve"],
                                "amount_remained" : balance}
                    response_errors = []
                    
                    self.action_done.emit(sender, response,response_errors, action_type)
                    
                    return
                else:
                    pass
                    ##response_errors = [ERRRRRROR]
                    ##self.action_done.emit(sender, response,response_errors, action_type)
                                        
            elif action_type == ACTIONS.Withdraw:
                if(self.__operations_executor.withdraw(data["currency"],data["reciever"],data["amount"])):
                    
                    self.__balance_inforation_configurator.take_into_account_btc_outflow(data["currency"],data["amount"])
                    
                    response_errors = []
                    response = {"currency": data["currency"],
                                "amount": data["amount"],
                                "reciever" : data["reciever"]}
                    
                    self.action_done.emit(sender, response, response_errors, action_type)
                     
                                
                