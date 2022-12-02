from akwizytor import Akwizytor
from decimal import Decimal

class AkwizytorNaEtacie(Akwizytor):
    """
    pracownik, który oprócz prowizji od sprzedaży otrzymuje stałą pensję....
    """
    def __init__(self,imie,nazwisko,nr_ubepzieczenia,sprzedaz,prowizja,pensja):
        super().__init__(imie,nazwisko,nr_ubepzieczenia,sprzedaz,prowizja)
        self.pensja = pensja


    @property
    def pensja(self):
        return self._pensja

    @pensja.setter
    def pensja(self,kwota):
        if kwota <Decimal('0.00'):
            raise ValueError('wyngrodzenie ryczałtowe nie może być ujemne')
        self._pensja = kwota

    def zrobek(self):
        return super().zrobek() + self.pensja

    def __repr__(self):
        return (f'etatowy {super().__repr__()}\nryczałt: {self.pensja:.2f}')


