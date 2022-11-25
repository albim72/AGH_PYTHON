from decimal import Decimal

class Akwizytor:

    """
    pracownik, którego wynagrodzenie jest wyłącznie prowizją od sprzedaży
    """

    def __init__(self,imie,nazwisko,nr_ubezpieczenia,sprzedaz,prowizja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_ubezpieczenia = nr_ubezpieczenia
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja
        
    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def nr_bezpieczenia(self):
        return self._nr_bezpieczenia

    @property
    def sprzedaz(self):
        return self._sprzedaz
        
        
        
        
        
