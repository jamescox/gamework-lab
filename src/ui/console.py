from PySide.QtGui import QLineEdit

from dockwidget import DockWidget


class Console(DockWidget):

    def __init__(self, player):
        DockWidget.__init__(self)
        
        self.__player = player
        
        getline = self.__getline = QLineEdit()
        getline.returnPressed.connect(self.execute)
        
        self.setWidget(getline)
        
        self.setWindowTitle('Console')
        
    
    def execute(self):
        command = self.__getline.text()
        
        print(command)
        print(self.__player.evaluate(command))
        
        self.__getline.setText('')
