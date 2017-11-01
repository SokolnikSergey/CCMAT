from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QIODevice
import sys

class QSer():
    def __init__(self):
        self.s = QSerialPort()

        self.s.setPortName("COM1")
        self.s.setBaudRate(QSerialPort.Baud9600)
        self.s.setParity(QSerialPort.EvenParity)
        self.s.setStopBits(QSerialPort.OneStop)
        if(not self.s.open(QIODevice.ReadOnly)):
            print("Not connected")
        else:
            self.s.readyRead.connect(self.onReadyRead)

    def onReadyRead(self):
        print(self.s.readAll())


app = QApplication([])

s = QSer()


sys.exit(app.exec_())

