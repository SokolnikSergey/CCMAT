from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMouseEvent, QFont
from PyQt5.Qt import Qt, pyqtSignal

class ImageButton(QLabel):

    clicked = pyqtSignal()

    def __init__(self, text, img_path):
        super(ImageButton, self).__init__(text)
        self.__crypt_name = text
        self.__image_path = img_path
        self.__currency = ""

        self.__default_color = "rgb(66, 101, 244);"
        self.__pressed_color = "rgb(87, 119, 249);"

        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("Segoe UI", 20))
        self.setStyleSheet("border-radius: 10px; color: white; background: " + self.__default_color)

    def setCryptName(self, text):
        self.setText("<img src=\""+self.__image_path+"\"><br>"+text+"<br>"+self.__currency)

    def setCurrency(self, new_currency):
 
        self.__currency = new_currency
        self.setCryptName(self.__crypt_name)

    def setDefaultColor(self, rgb_color):
        self.__default_color = rgb_color

    def setPressedColor(self, rgb_color):
        self.__pressed_color = rgb_color

    def getCryptName(self):
        return self.__crypt_name

    def mousePressEvent(self, event):
        self.setStyleSheet("border-radius: 10px; color: white; background: "+self.__pressed_color)

    def mouseReleaseEvent(self, event):
        self.setStyleSheet("border-radius: 10px; color: white; background: "+self.__default_color)
        self.clicked.emit()