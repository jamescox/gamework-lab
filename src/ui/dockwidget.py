from PySide.QtGui import QAction, QDockWidget


class DockWidget(QDockWidget):

    def __init__(self, parent=None):
        QDockWidget.__init__(self, parent)

        show_hide = self.__show_hide = QAction(self)
        show_hide.triggered.connect(self.toggle_visibility)
        
        self.__updateActionTitle()
    
    
    @property
    def show_hide(self): return self.__show_hide
    
    
    def toggle_visibility(self):
        self.setVisible(not self.isVisible())
    
    
    def showEvent(self, event):
        self.__updateActionTitle()
        
    def hideEvent(self, event):
        self.__updateActionTitle()
        
        
    def __updateActionTitle(self):
        if self.isVisible():
            self.show_hide.setText('Hide &' + self.windowTitle())
        else:
            self.show_hide.setText('Show &' + self.windowTitle())
