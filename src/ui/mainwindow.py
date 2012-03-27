try:
    from PySide.QtCore import Qt
    from PySide.QtGui  import QAction, QKeySequence, QMainWindow, QMdiArea
except ImportError:
    from PyQt4.QtCore import Qt
    from PyQt4.QtGui  import QAction, QKeySequence, QMainWindow, QMdiArea

from project.project import Project

from ui.codeeditor      import CodeEditor
from ui.console         import Console
from ui.gameplayer      import GamePlayer
from ui.projectoutline  import ProjectOutline
from ui.revisioncontrol import RevisionControl

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, None)
        
        editor = self.__editor = CodeEditor()
        
        project = self.__project = Project()
        
        editor.setDocument(project.main_js)
        
        outline   = self.__outline   = ProjectOutline(project)
        player    = self.__player    = GamePlayer(project)
        console   = self.__console   = Console(player)
        revisions = self.__revisions = RevisionControl(project)
        
        self.addDockWidget(Qt.LeftDockWidgetArea,  outline)
        self.addDockWidget(Qt.LeftDockWidgetArea,  revisions)
        self.addDockWidget(Qt.RightDockWidgetArea, player)
        self.addDockWidget(Qt.RightDockWidgetArea, console)
        
        self.setCentralWidget(editor)
        self.setWindowTitle('GameWork Lab')
        
        view_menu = self.menuBar().addMenu('&View')
        view_menu.addAction(console.show_hide)
        view_menu.addAction(outline.show_hide)
        view_menu.addAction(player.show_hide)
        view_menu.addAction(revisions.show_hide)
        
        run_menu     = self.menuBar().addMenu('&Run')
        restart_game = run_menu.addAction('Restart Game')
        restart_game.setShortcut(QKeySequence('F5'))
        restart_game.triggered.connect(self.restart_game)
        
        
    def restart_game(self):
        self.__project.save('As run on ')
        self.__player.restart()
        
