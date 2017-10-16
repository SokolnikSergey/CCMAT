from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QApplication
from PyQt5.Qt import Qt, QTranslator
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDateTime, QTimer, QTime, QDate
from LangButton import LangButton

class WindowContainer(QWidget):

    def __init__(self):
        super(WindowContainer, self).__init__()
        self.create_objects()
        self.prepare_layouts()
        self.config_header_widgets()
        self.update_time()

    def create_objects(self):

        self.__vlay_main = QVBoxLayout()
        self.__hlay_header = QHBoxLayout()

        self.__label_time = QLabel("<time>")
        self.__label_lang = LangButton()

        self.__contain_window_ptr = None

        self.__timer_updater = QTimer()

        self.__timer_updater.timeout.connect(self.update_time)
        self.__timer_updater.start(1000)



    def prepare_layouts(self):

        self.__vlay_main.addLayout(self.__hlay_header)
        self.__vlay_main.setContentsMargins(0,0,0,0)
        self.__vlay_main.setSpacing(0)

        self.__hlay_header.addWidget(self.__label_time)
        self.__hlay_header.addWidget(self.__label_lang)
        self.__hlay_header.setSpacing(0)

        self.setLayout(self.__vlay_main)

    def set_contain_window(self, window):
        if(self.__contain_window_ptr != None):

            self.__vlay_main.removeWidget(self.__contain_window_ptr)
            self.__contain_window_ptr.close()
            self.__contain_window_ptr.deleteLater()
            self.__contain_window_ptr = None

        self.__vlay_main.addWidget(window)
        self.__contain_window_ptr = window
        window.on_close.connect(self.set_contain_window)
        window.show()

    def config_header_widgets(self):
        self.__label_time.setAlignment(Qt.AlignVCenter)
        self.__label_time.setContentsMargins(10, 0, 0, 0)
        self.__label_lang.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.__label_lang.setContentsMargins(0, 0, 10, 0)
        self.__label_time.setFixedHeight(50)
        self.__label_lang.setFixedSize(50, 50)
        self.__label_time.setFont(QFont("Segoe UI", 15))
        self.__label_lang.setFont(self.__label_time.font())
        self.__label_lang.add_language("ru", "images/flags/ru.png")
        self.__label_lang.add_language("en", "images/flags/us.png")
        self.__label_lang.languageChanged.connect(self.language_changed)
        self.__label_lang.setStyleSheet("background: rgb(225,225,225);")
        self.__label_time.setStyleSheet("background: rgb(225,225,225);")


    def update_time(self):
        datetime = QDateTime.currentDateTime()
        date = datetime.date()
        time = datetime.time()
        self.__label_time.setText("{0}.{1}.{2}, {3}:{4}".format(date.day(), date.month(), date.year(), time.hour(), time.minute()))

    def language_changed(self, lang):
        print(lang)