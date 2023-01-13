from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication,QWidget
from gui import Ui_Widget
import sys

class Widgety(QWidget,Ui_Widget):
    def __init__(self,parent=None):
        super(Widgety,self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()
    sys.exit(app.exec_())
