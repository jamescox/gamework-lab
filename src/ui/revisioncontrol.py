try:
    from PySide.QtGui import QComboBox, QLineEdit, QToolBar
except ImportError:
    from PyQt4.QtGui import QComboBox, QLineEdit, QToolBar
    
from dockwidget import DockWidget 


class RevisionControl(DockWidget):
    
    def __init__(self, project):
        DockWidget.__init__(self)
        
        self.__project = project
        
        self.setWindowTitle('Revisions')