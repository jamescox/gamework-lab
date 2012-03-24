from PySide.QtCore   import QUrl
from PySide.QtWebKit import QWebView

from dockwidget import DockWidget


class GamePlayer(DockWidget):

    def __init__(self, parent=None):
        DockWidget.__init__(self, parent)
        
        webview = self.__webview = QWebView()
        webview.load(QUrl.fromLocalFile('/home/jcx/Projects/gamework.js/build/template/index.html'))
        
        self.setWidget(webview)

        self.setWindowTitle('Player')

            
    def evaluate(self, code):
        self.__webview.page().mainFrame().evaluateJavaScript(code);
