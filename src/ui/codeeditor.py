from PySide.QtGui import QPlainTextEdit


class CodeEditor(QPlainTextEdit):

    def __init__(self):
        QPlainTextEdit.__init__(self)
        
        self.setWindowTitle('main.js')
