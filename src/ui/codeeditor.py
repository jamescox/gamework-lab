try:
    from PySide.QtGui import QPlainTextEdit
except ImportError:
    from PyQt4.QtGui import QPlainTextEdit
    
    
class CodeEditor(QPlainTextEdit):

    def __init__(self):
        QPlainTextEdit.__init__(self)
        
        self.setStyleSheet('QPlainTextEdit { font-family: monospace; }')
        
        self.setWindowTitle('main.js')
