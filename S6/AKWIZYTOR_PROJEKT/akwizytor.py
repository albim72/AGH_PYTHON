from decimal import Decimal

class Akwizytor:
    """
    akwizytor- pracownik którego dochód obliczany jest na podstawie prowizji od sprzedaży
    """
    def __init__(self,imie,nazwisko,nr_ubepzieczenia,sprzedaz,prowizja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_ubepzieczenia = nr_ubepzieczenia
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja
        
    @property
    def imie(self):
        return self._imie
    
    @property
    def nazwisko(self):
        return self._nazwisko
    
    @property
    def nr_ubepieczenia(self):
        return self._nr_ubepzieczenia
    
    @property
    def sprzedaz(self):
        return self._sprzedaz
    
    @sprzedaz.setter
    def sprzedaz(self,kwota):
        if kwota < Decimal('0.00'):
            raise ValueError('wartość sprzedaży nie może być ujemna')
        self._sprzedaz = kwota
        
    @property
    def prowizja(self):
        return self._prowizja
    
    @prowizja.setter
    def prowizja(self,procent):
        if not (Decimal('0.0')<procent<Decimal('100.0')):
            raise ValueError('prowizja nie może być ujemna ale też nie może wynosić 100% lub więcej...')
        self._prowizja = procent
        
    def zrobek(self):
        return self.sprzedaz*(self.prowizja/Decimal('100.0'))
    
    def __repr__(self):
        return (f'Akwizytor: {self.imie} {self.nazwisko}\nnumer ubezpieczenia: {self.nr_ubepzieczenia}\n'
                f'sprzedaż: {self.sprzedaz:.2f}\nprowizja: {self.prowizja:.2f}%')
        
        
        
        
        
