from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QGridLayout,\
    QLineEdit,QPushButton,QHBoxLayout,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class Kalkulator(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.interfejs()

    def koniec(self):
        self.close()

    def closeEvent(self, event) -> None:
        odp = QMessageBox.question(
            self,'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_Escape:
            self.close()
            
            
    def dzialanie(self):
        nadawca = self.sender()
        try:
            liczbaa = float(self.liczbaaEdit.text())
            liczbab = float(self.liczbabEdit.text())
            wynik = ""
            
            if nadawca.text() == "&Dodaj":
                wynik = liczbaa + liczbab
            elif nadawca.text() == "&Odejmij":
                wynik = liczbaa - liczbab
            elif nadawca.text() == "&Mnóż":
                wynik = liczbaa * liczbab
            else:
                try:
                    wynik = round(liczbaa/liczbab,9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self,'Błąd',"Nie można dzielić przez 0!"
                    )
            self.wynikEdit.setText(str(wynik))
        except ValueError:
            QMessageBox.warning(self,'Błąd','Błędne dane',QMessageBox.Ok)

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

        #1liniowe pola edycyjne
        self.liczbaaEdit = QLineEdit()
        self.liczbabEdit = QLineEdit()
        self.wynikEdit = QLineEdit()

        self.wynikEdit.readonly = True
        self.wynikEdit.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')
        ukladT.addWidget(self.liczbaaEdit,1,0)
        ukladT.addWidget(self.liczbabEdit,1,1)
        ukladT.addWidget(self.wynikEdit,1,2)

        #przyciski
        dodajBtn = QPushButton("&Dodaj",self)
        odejmijBtn = QPushButton("&Odejmij",self)
        dzielBtn = QPushButton("&Dziel",self)
        mnozBtn = QPushButton("&Mnóż",self)
        koniecBtn = QPushButton("&Koniec",self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(mnozBtn)
        ukladH.addWidget(dzielBtn)

        ukladT.addLayout(ukladH,2,0,1,3)
        ukladT.addWidget(koniecBtn,3,0,1,3)


        #przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        koniecBtn.clicked.connect(self.koniec)
        
        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        mnozBtn.clicked.connect(self.dzialanie)
        dzielBtn.clicked.connect(self.dzialanie)

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
