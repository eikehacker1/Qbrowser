from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def go_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def go_home(self):
        self.browser.setUrl(QUrl('htpps://google.com'))
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
         
        #navigation of bar 
        navbar = QToolBar(self)
        navbar.setGeometry(1200, 1300, 1500, 1200)
        self.addToolBar(navbar)
        voltar_btn = QAction('⬅', self)
        voltar_btn.triggered.connect(self.browser.back)
        navbar.addAction(voltar_btn)

        #follow button
        fl_btn = QAction('➡️',  self)
        fl_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fl_btn)

        #refresh button
        refresh_btn = QAction('🔃', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)
        #home button 
        home_btn = QAction('🏫', self)
        home_btn.triggered.connect(self.go_home)
        navbar.addAction(home_btn)
        #nave bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)



app = QApplication(sys.argv)
QApplication.setApplicationName('QBROW')
windows = MainWindow()

app.exec()

