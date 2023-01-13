from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QGridLayout
from PyQt5.QtGui import QIcon
import sys

class Kalkulator(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):

        #etykiety
        etykieta1 = QLabel("liczba a:",self)
        etykieta2 = QLabel("liczba b:",self)
        etykieta3 = QLabel("wynik:",self)

        #przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1,0,0)
        ukladT.addWidget(etykieta2,0,1)
        ukladT.addWidget(etykieta3,0,2)

        #przypisanie utworzonego układu do okna
        self.setLayout(ukladT)
        self.setGeometry(20,20,300,100)
        self.setWindowIcon(QIcon('name.jpg'))
        self.setWindowTitle("Prosty kalkulator")
        # self.resize(300,100)
        # self.setWindowTitle("Prosty kalkulator")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())
