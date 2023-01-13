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
