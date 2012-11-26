# -*- encoding: utf-8 -*-
import os, sys
from PyQt4.QtGui import QApplication
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    sys.exit(app.exec_())
