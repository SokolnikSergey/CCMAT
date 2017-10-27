from PyQt5.QtCore import QObject,pyqtSignal
import os


class QRController(QObject):
	qr_detected = pyqtSignal(str)

	def __init__(self, path_to_file = "ZBar/qr1.jpg"):
		super(QRController, self).__init__()
		self.__path_to_file = path_to_file

	def search_qr_data_token(self):
		print(os.getcwd())
		command = r'{path_to_zbar} --raw {path}'.format(path=self.__path_to_file, path_to_zbar=os.getcwd()+"/ZBar/zbarimg.exe")
		qr_text = os.popen(command).read()
		if(len(qr_text)):
			print("qr_decoded")
			self.qr_detected.emit(qr_text)
			print("qr_decode(1)")
			self.deletePhoto()

	def deletePhoto(self):
		if(os.path.exists(os.getcwd()+"/ZBar/qr1.jpg")):
			os.remove(os.getcwd()+"/ZBar/qr1.jpg")