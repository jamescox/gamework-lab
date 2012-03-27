import os

try:
    from PySide.QtCore   import QUrl, QSize
    from PySide.QtGui    import QAction
    from PySide.QtWebKit import QWebView
except ImportError:
    from PyQt4.QtCore   import QUrl, QSize
    from PyQt4.QtGui    import QAction
    from PyQt4.QtWebKit import QWebView

from dockwidget import DockWidget


class GamePlayer(DockWidget):

    def __init__(self, project, parent=None):
        DockWidget.__init__(self, parent)
        
        self.__project = project
        
        webview = self.__webview = QWebView()
        webview.settings().clearMemoryCaches()
        
        webview.load(project.game_url)
        
        self.setWidget(webview)

        self.setWindowTitle('Player')


    def sizeHint(self):
        return QSize(400, 400)
        
        
    def restart(self):
        self.__webview.settings().clearMemoryCaches()
        self.__webview.reload()


    def evaluate(self, code):
        self.__webview.page().mainFrame().evaluateJavaScript(code);
