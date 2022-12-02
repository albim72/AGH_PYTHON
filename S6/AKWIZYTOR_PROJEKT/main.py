from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class DuzaFirma:

    def __repr__(self):
        return 'Mam dużą firmę i wielką prowizję...'
    def zarobek(self):
        return Decimal('1_000_000.00')

k = DuzaFirma()
s = AkwizytorNaEtacie("Robert","Kłak","3444-554-4554",Decimal('235000.00'),Decimal('7.5'),Decimal('4500.00'))
c = Akwizytor("Olga","Nomi","5656-45656",Decimal('789400.00'),Decimal('9.9'))

pracownicy = [c,s,k]

for prac in pracownicy:
    print(prac)
    print(f'{prac.zarobek():,.2f}\n')
