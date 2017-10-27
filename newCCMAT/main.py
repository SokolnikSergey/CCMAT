from PyQt5.QtWidgets import QApplication
from WindowContainer import WindowContainer
from MainWindow import MainWindow
from Button import ImageButton
from BuyCoinsWindow import BuyCoinsWindow
from QRScannerUI import QRScannerUI
from PyQt5.QtWidgets import QDesktopWidget
import sys

app = QApplication(sys.argv)

container = WindowContainer()

container.set_contain_window(MainWindow())
container.showFullScreen()
sys.exit(app.exec_())
