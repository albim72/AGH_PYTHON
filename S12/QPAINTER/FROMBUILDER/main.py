from PyQt5.QtWidgets import QApplication,QWidget
import sys
from simple import Ui_Dialog

class Okienko(QWidget,Ui_Dialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okienko()
    sys.exit(app.exec_())
