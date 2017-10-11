from Interfaces.SessionDataSubscriber import SessionDataSubscriber

class SDSubs(SessionDataSubscriber):
	def __init__(self):
		pass
	
	def remaining_money_on_server_update(self, new_ramain_money):
		print("REMAINING_MONEY_ON_SERVER_updateD->",new_ramain_money )
		
	def currency_for_operation_update(self, new_currency_for_operation):
		print("currency_for_operation_updateD->",new_currency_for_operation )
	
	
	def recieved_money_update(self, new_recieved_money):
		print("recieved_money_updated->", new_recieved_money)
	
	def transactions_fee_update(self, new_transactions_fee):
		print("transactions_fee_updated->", new_transactions_fee)
	
	def reciever_address_update(self, new_reciever_address):
		print("reciever_address_updated->", new_reciever_address)
	