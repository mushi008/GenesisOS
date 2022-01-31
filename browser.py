import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import speech_recognition as sr


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('←', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('→', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        Reload_btn = QAction('↵', self)
        Reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(Reload_btn)

        Home_btn = QAction('🏠', self)
        Home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(Home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigat_to_url)
        navbar.addWidget(self.url_bar)
        url = self.url_bar

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://www.google.com'))

    def navigat_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    var = sr.Microphone
App = QApplication(sys.argv)
QApplication.setApplicationName('MUSHI Browser')
Window = MainWindow()
qApp.exec()
