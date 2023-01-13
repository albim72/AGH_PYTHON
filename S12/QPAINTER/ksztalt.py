from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import QRect, QPoint, QSize
from gui import Ksztalty

class Ksztalt(QWidget):

    """Klasa definiująca Widget do rysowania kształtów"""
    #współrzędne prostokąta i trójkta
    prost = QRect(1,1,101,101)
    punkty = QPolygon([
        QPoint(1,101),
        QPoint(51,1),
        QPoint(101,101)
    ])

    def __init__(self,parent,ksztalt =Ksztalty.Rect):
        super(Ksztalt,self).__init__(parent)
        self.ksztalt = ksztalt
        self.kolor0 = QColor(0,0,0)
        self.kolorW = QColor(255,255,255)

    def paintEvent(self, e) -> None:
        qp = QPainter()
        qp.begin(self)
        self.rysujFigury(e,qp)
        qp.end()

    def rysujFigury(self,e,qp):
        qp.setPen(self.kolorO)
        qp.setBrush(self.kolorW)
        qp.setRenderHint(QPainter.Antialiasing)
        if self.ksztalt == Ksztalty.Rect:
            qp.drawRect(self.prost)
        elif self.ksztalt == Ksztalty.Ellipse:
            qp.drawEllipse(self.prost)
        elif self.ksztalt == Ksztalty.Polygon:
            qp.drawPolygon(self.punkty)
        elif self.ksztalt == Ksztalty.Line:
            qp.drawLine(self.prost.topLeft(),self.prost.bottomRight())
        else:
            qp.drawRect(self.prost)

    def sizeHint(self):
        return QSize(102,102)

    def minimumSizeHint(self):
        return QSize(102, 102)

    def ustawKsztalt(self,ksztalt):
        self.ksztalt = ksztalt
        self.update()

    def ustawKolorW(self,r=0,g=0,b=0):
        self.kolorW = QColor(r,g,b)
        self.update()
