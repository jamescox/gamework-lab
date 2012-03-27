from ui.mainwindow import MainWindow


if __name__ == '__main__':
    import sys
    
    try:
        from PySide.QtGui import QApplication
    except ImportError:
        from PyQt4.QtGui import QApplication
      
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec_())
