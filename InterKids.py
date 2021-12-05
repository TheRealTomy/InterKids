import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow) :
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QtWebEngineView()
        self.browser.setUrl(QUrl('https://www.kiddle.co'))
        self.setCentralWidget(self.browser)
        self.showMaximized


app = QApplication(sys.argv)
QApplication. setApplicationName('InterKids')
window = MainWindow
app.exec_()