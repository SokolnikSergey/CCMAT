from PyQt5.QtCore import QObject,pyqtSignal
import os


class QRController(QObject):
	
	qr_detected = pyqtSignal(str)
	
	def __init__(self,path_to_file = "../qr.jpg"):
		super(QRController, self).__init__()
		self.__path_to_file = path_to_file
	

	def search_qr_data_token(self):
		
		command = r'"C:/Program Files (x86)/ZBar/bin/zbarimg.exe" --raw {path}'.format(path=self.__path_to_file)
		qr_text = os.popen(command).read()
		
		self.qr_detected.emit(qr_text)