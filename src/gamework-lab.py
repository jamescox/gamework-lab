from ui.mainwindow import MainWindow


if __name__ == '__main__':
    import sys
    
    from PySide.QtGui import QApplication
    
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec_())
