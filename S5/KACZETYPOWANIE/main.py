from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class Wlasciciel:

    def __repr__(self):
        return "jestem właścicielem biznesu, więc się bogacę...."

    def zarobek(self):
        return Decimal('1_000_000.00')


k = Wlasciciel()
s = AkwizytorNaEtacie('Robert','Nowak','56456365534545',Decimal('167000.00'),Decimal('8'),Decimal('3000.00'))
c = Akwizytor('Olga','Nowak','8567545555656',Decimal('2340000.00'),Decimal('9'))

pracownicy = [k,s,c]

for prac in pracownicy:
    print(prac)
    print(f'{prac.zarobek():,.2f}\n')
