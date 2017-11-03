import configparser,os

class InformationFiller:
	
	def __init__(self,aux_info_container = None,path_to_ini = "../../owners_info.ini"):
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
		self.__config_parser.set("Settings","wallet_address","-1")
		
		self.__config_parser.add_section("AccountData")
		
		self.__config_parser.set( "AccountData", "API_KEY", "-1")
		self.__config_parser.set("AccountData", "SECRET_KEY", "-1")

		self.__config_parser.add_section("Support")

		self.__config_parser.set("Support", "SupportNumber", "-1")

		self.__config_parser.add_section("Support")

		self.__config_parser.set("Support", "TestMode", "1")

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
	
	def read_api_key_from_ini(self):
		api_key = None
		if self.__config_parser is not None:
			if "AccountData" in self.__config_parser:
				api_key = self.__config_parser["AccountData"]["API_KEY"]
				if (api_key is not None) and self.___aux_information_container:
					print(api_key)
					self.___aux_information_container.api_key = api_key
		return api_key
		
		
	def read_secter_key_from_ini(self):
		secret_key = None
		if self.__config_parser is not None:
			if "AccountData" in self.__config_parser:
				secret_key = self.__config_parser["AccountData"]["SECRET_KEY"]
				if (secret_key is not None) and self.___aux_information_container:
					print(secret_key)
					self.___aux_information_container.secret_key = secret_key
		return secret_key

	def read_wallet_address_from_ini(self):
		wallet_address = None
		if self.__config_parser is not None:
			if "Settings" in self.__config_parser:
				wallet_address = self.__config_parser["Settings"]["wallet_address"]
				if (wallet_address is not None) and self.___aux_information_container:
					print(wallet_address)
					self.___aux_information_container.wallet_address = wallet_address
		return wallet_address

	def read_support_number_from_ini(self):
		support_number = None
		if self.__config_parser is not None:
			if "Support" in self.__config_parser:
				support_number = self.__config_parser["Support"]["SupportNumber"]
				if (support_number is not None) and self.___aux_information_container:
					print(support_number)
					self.___aux_information_container.support_number = support_number

		return support_number
	

	def read_test_mode_from_ini(self):
		test_mode = None
		if self.__config_parser is not None:
			if "Support" in self.__config_parser:
				test_mode = self.__config_parser["Support"]["TestMode"]
				if (test_mode is not None) and self.___aux_information_container:
					print(test_mode)
					self.___aux_information_container.test_mode = test_mode
		return test_mode

	def fill_container_by_file_data(self):
		self.read_owners_fee_from_ini()
		self.read_api_key_from_ini()
		self.read_secter_key_from_ini()
		self.read_wallet_address_from_ini()
		self.read_support_number_from_ini()
		self.read_test_mode_from_ini()
