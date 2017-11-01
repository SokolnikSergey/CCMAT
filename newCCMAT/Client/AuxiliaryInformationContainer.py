
class AuxiliaryInformationContainer():
	def __init__(self,imei = "",location="",host_server = ""):
	
		self.__imei = imei
		self.__location = location
		self.__host_server = host_server

	@property
	def host_server(self):
		return self.__host_server

	@host_server.setter
	def host_server(self, new_host_server):
		if (new_host_server and isinstance(new_host_server, str)):
			self.__host_server = new_host_server
		
	@property
	def imei(self):
		return self.__imei
	
	@imei.setter
	def imei(self,new_imei):
		if (new_imei and isinstance(new_imei,str)):
			self.__imei = new_imei
			
	@property
	def location(self):
		return self.__location
	
	@location.setter
	def location(self,new_location):
		if (new_location and isinstance(new_location,str)):
			self.__location = new_location
	
	
			
				
			
			