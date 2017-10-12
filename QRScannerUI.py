from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QCameraImageCapture
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.Qt import Qt, QTimer, pyqtSignal
class QRScannerUI(QWidget):

    qr_decoded = pyqtSignal(str)

    def __init__(self):
        super(QRScannerUI, self).__init__()
        self.createObjects()
        self.configObjects()

    def createObjects(self):
        self.__vlay_main = QVBoxLayout()

        self.__label_status = QLabel()

        self.__camera = self.__getCamera()
        self.__viewfinder = QCameraViewfinder()

        self.__timer = QTimer()

        if(self.__camera):
            self.__camera_capture = QCameraImageCapture(self.__camera)



    def configObjects(self):

        self.setLayout(self.__vlay_main)
        self.__label_status.setAlignment(Qt.AlignCenter)

        self.__vlay_main.addWidget(self.__label_status)
        self.__vlay_main.addWidget(self.__viewfinder)

        self.__timer.timeout.connect(self.__capturing)

        if (self.__camera):
            self.__camera.setViewfinder(self.__viewfinder)
            self.__camera.start()
            self.__timer.start(1000)


    def __getCamera(self):
        if(len(QCameraInfo.availableCameras()) > 0):
            return QCamera(QCameraInfo.availableCameras()[0])
        else:
            self.__label_status.setText("Камера не обнаружена")

    def __capturing(self):
        self.__camera.searchAndLock()
        self.__camera_capture.capture("1")
        self.__camera.unlock()
        self.__camera.stop()
        self.__scanning_success()

    def __scanning_success(self):
        self.qr_decoded.emit("qweqwesdfsdfsdf123dfsdfsdsdfsd")