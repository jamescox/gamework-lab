from PySide.QtCore import Qt
from PySide.QtGui  import QAction, QMainWindow, QMdiArea

from ui.gameplayer import GamePlayer
from ui.console    import Console
from ui.codeeditor import CodeEditor


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, None)
        
        mdi_area = self.__mdi_area = QMdiArea()
        mdi_area.setViewMode(QMdiArea.TabbedView)
        
        player  = self.__player  = GamePlayer()
        console = self.__console = Console(player)
        
        self.addDockWidget(Qt.RightDockWidgetArea, player)
        self.addDockWidget(Qt.RightDockWidgetArea, console)
        
        self.setCentralWidget(mdi_area)
        self.setWindowTitle('GameWork Lab')
        
        view_menu = self.menuBar().addMenu('&View')
        view_menu.addAction(console.show_hide)
        view_menu.addAction(player.show_hide)
        
        mdi_area.addSubWindow(CodeEditor())
        mdi_area.addSubWindow(CodeEditor())
        #mdi_area.addSubWindow(CodeEditor())

    
