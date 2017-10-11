import configparser,os

class InformationFiller:
	
	def __init__(self,aux_info_container = None,path_to_ini = "../owners_info.ini"):
		self.__config_parser = None
		self.__path_to_ini = path_to_ini
		self.___aux_information_container = aux_info_container
		
		self.create_config_parser()
		self.read_from_config_file()
		
		
		
	def create_config_parser(self):
		self.__config_parser = configparser.ConfigParser()
	
	def read_from_config_file(self):
		if self.__config_parser is not None:
			if (os.path.exists(self.__path_to_ini)):
				self.__config_parser.read(self.__path_to_ini)
			else:
				self.set_default_values()
				self.__config_parser.read(self.__path_to_ini)
	
	def set_default_values(self):
		self.__config_parser.add_section("Settings")
		
		self.__config_parser.set("Settings", "Owners_fee", "0.02")
		
		self.write_to_config_file()
	
	def write_to_config_file(self):
		if self.__config_parser is not None:
			with open(self.__path_to_ini, "w") as config_file:
				self.__config_parser.write(config_file)
	
	def read_owners_fee_from_ini(self):
		owners_fee = None
		if self.__config_parser is not None:
			if "Settings" in self.__config_parser:
				owners_fee = self.__config_parser["Settings"]["Owners_fee"]
				if (owners_fee is not None) and self.___aux_information_container:
					print(owners_fee)
					self.___aux_information_container.owners_fee = owners_fee
		return owners_fee

	def fill_container_by_file_data(self):
		self.read_owners_fee_from_ini()
