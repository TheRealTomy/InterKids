import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.kiddle.co'))
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QIcon('icon.ico'))
        self.showMaximized()

        # navbar (controls and that stuff)
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward = QAction('Forward', self)
        forward.triggered.connect(self.browser.forward)
        navbar.addAction(forward)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        games_btn = QAction('Games', self)
        games_btn.triggered.connect(self.games_btn)
        navbar.addAction(games_btn)

        music_btn = QAction('Music', self)
        music_btn.triggered.connect(self.music_btn)
        navbar.addAction(music_btn)

    def games_btn(self):
        self.browser.setUrl(QUrl('https://www.abcya.com'))

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.kiddle.co'))

    def music_btn(self):
        self.browser.setUrl(QUrl('https://www.ñclassicsforkids.com'))


app = QApplication(sys.argv)
QApplication.setApplicationName('InterKids')
window = MainWindow()
app.exec_()
