from Interfaces.AuxiliaryInformationPublisher import AuxiliaryInformationPublisher

class AuxiliaryInformationContainer(AuxiliaryInformationPublisher):
	def __init__(self,owners_fee = -1):
		self.__owners_fee = owners_fee
		
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
	
	def update_owners_fee(self):
		for subs in self.__subscribers:
			subs.updated_owners_fee(self.__owners_fee)
	
	def subscribe(self, subscriber):
		if subscriber not in self.__subscribers:
			self.__subscribers.append(subscriber)
		
	def unsubscribe(self, subscriber):
		if subscriber in self.__subscribers:
			self.__subscribers.remove(subscriber)

	
			
				
			
			