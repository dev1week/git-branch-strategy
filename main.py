import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,
                             QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import QIcon

        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    view=Calculator()
    sys.exit(app.exec_())