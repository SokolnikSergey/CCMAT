from Interfaces.AuxiliaryInformationPublisher import AuxiliaryInformationPublisher

class AuxiliaryInformationContainer(AuxiliaryInformationPublisher):
	def __init__(self,owners_fee = -1,api_key = None,secret_key=None):
		self.__owners_fee = owners_fee
		
		self.__api_key = api_key,
		self.__secret_key = secret_key
		
		self.__subscribers =[]
		
	@property
	def owners_fee(self):
		return self.__owners_fee
	
	@owners_fee.setter
	def owners_fee(self,new_owners_fee):
		if (new_owners_fee and isinstance(new_owners_fee,(int,float))):
			self.__owners_fee = new_owners_fee
	
		if (new_owners_fee and isinstance(new_owners_fee,str)):
			try:
				self.__owners_fee = float(new_owners_fee)
			except Exception as ex:
				pass
			
	@property
	def api_key(self):
		return self.__api_key
	
	@api_key.setter
	def api_key(self,new_api_key):
		self.__api_key = new_api_key
	
	@property
	def secret_key(self):
		return self.__secret_key
	
	@secret_key.setter
	def secret_key(self, new_secret_key):
		self.__secret_key = new_secret_key
	
	def update_owners_fee(self):
		for subs in self.__subscribers:
			subs.updated_owners_fee(self.__owners_fee)
	
	def subscribe(self, subscriber):
		if subscriber not in self.__subscribers:
			self.__subscribers.append(subscriber)
		
	def unsubscribe(self, subscriber):
		if subscriber in self.__subscribers:
			self.__subscribers.remove(subscriber)

	
			
				
			
			