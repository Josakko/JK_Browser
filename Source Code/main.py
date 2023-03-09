import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        
        self.setWindowTitle("JK Browser")
        self.setWindowIcon(QIcon("JK.ico"))
        self.setGeometry(100, 100, 1400, 800)
        

        search_engine = self.show_search_engine_selection_popup()
        
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        
        if search_engine == "Yandex":
            self.browser.setUrl(QUrl("https://www.yandex.com"))
        elif search_engine == "DuckDuckGo":
            self.browser.setUrl(QUrl("https://duckduckgo.com"))
        elif search_engine == "Bing":
            self.browser.setUrl(QUrl("https://www.bing.com"))
        elif search_engine == "Google":
            self.browser.setUrl(QUrl("https://www.google.com"))
        elif search_engine  == "Ahmia":
            self.browser.setUrl(QUrl("http://ahmia.fi"))
        elif search_engine == "None":
            self.browser.setUrl(QUrl())
        
        self.back_button = QPushButton("<")
        self.forward_button = QPushButton(">")
        self.refresh_button = QPushButton("Refresh")
        self.url_bar = QLineEdit()
        
        toolbar = QToolBar()
        toolbar.addWidget(self.back_button)
        toolbar.addWidget(self.forward_button)
        toolbar.addWidget(self.refresh_button)
        toolbar.addWidget(self.url_bar)
        self.addToolBar(toolbar)
        

        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)
        self.refresh_button.clicked.connect(self.browser.reload)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.browser.urlChanged.connect(self.update_url_bar)
    
    def show_search_engine_selection_popup(self):
        options = ["Yandex", "DuckDuckGo", "Bing", "Google", "Ahmia", "None"]
        selected_option, ok = QInputDialog.getItem(self, "Select search engine", "Select a search engine:", options, 0, False)
        if ok:
            return selected_option
        else:
            sys.exit(0)
            
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    
    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

