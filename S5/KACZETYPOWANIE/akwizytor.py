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

    @imie.setter
    def imie(self,imie):
        self._imie = imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @imie.setter
    def nazwisko(self, nazwisko):
        self._nazwisko = nazwisko

    @property
    def nr_bezpieczenia(self):
        return self._nr_bezpieczenia

    @imie.setter
    def nr_bezpieczenia(self, nr_bezpieczenia):
        self._nr_bezpieczenia = nr_bezpieczenia

    @property
    def sprzedaz(self):
        return self._sprzedaz


    @sprzedaz.setter
    def sprzedaz(self,kwota):
        if kwota < Decimal('0.00'):
            raise ValueError('Wartość sprzedaży nie może być ujemna')
        self._sprzedaz = kwota

    @property
    def prowizja(self):
        return self._prowizja

    @prowizja.setter
    def prowizja(self, procent):
        if not Decimal('0.0') < procent < Decimal('100.0'):
            raise ValueError('Prowizja nie może być ujemna i nie może przekraczać 100%')
        self._prowizja = procent


    def zarobek(self):
        return self.sprzedaz*(self.prowizja/Decimal('100.0'))

    def __repr__(self):
        """
        reprezentacja tesktowa obiektu
        """

        return (f"Akwizytor: {self.imie} {self.nazwisko}\nnumer ubezpieczenia: {self.nr_bezpieczenia}\n"
                f"sprzedaż: {self.sprzedaz:.2f}\nprowizja: {self.prowizja:.2f}%")
