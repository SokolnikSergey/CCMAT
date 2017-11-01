import configparser,os

class InformationFiller:
	
	def __init__(self,aux_info_container = None,path_to_ini = "../../bankomat_info.ini"):
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
		
		self.__config_parser.set("Settings", "IMEI", "123312imei")
		
		self.__config_parser.set("Settings", "LOCATION", "Odessa")

		self.__config_parser.set("Settings", "host_server", "localhost")

		self.write_to_config_file()

	def write_to_config_file(self):
		if self.__config_parser is not None:
			with open(self.__path_to_ini, "w") as config_file:
				self.__config_parser.write(config_file)

	def read_imei_from_ini(self):
		imei = None
		if self.__config_parser is not None:
			if "Settings" in self.__config_parser:
				imei = self.__config_parser["Settings"]["IMEI"]
				if (imei is not None) and self.___aux_information_container:
					self.___aux_information_container.imei = imei
		return imei

	def read_location_from_ini(self):
		location = None
		if self.__config_parser is not None:
			if "Settings" in self.__config_parser:
				location = self.__config_parser["Settings"]["LOCATION"]
				if (location is not None) and self.___aux_information_container:
					self.___aux_information_container.location = location
		return location

	def read_host_server(self):
		host_server = None
		if self.__config_parser is not None:
			if "Settings" in self.__config_parser:
				host_server = self.__config_parser["Settings"]["host_server"]
				print(host_server)
				if (host_server is not None) and self.___aux_information_container:
					self.___aux_information_container.host_server = host_server
		return host_server

	def fill_container_by_file_data(self):
		self.read_imei_from_ini()
		self.read_location_from_ini()
		self.read_host_server()