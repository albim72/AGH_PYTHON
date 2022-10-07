#import dane
#import dane as dn
from dane import book
from moje_funkcje.mff.funkcje12 import konferencja,gx
from miasto import Miasto

print(book)
print(book["autor"])

konferencja("Algorytmy AI - zastosowania w medycynie","Rzeszów","2022-10-11")
print(f"wynik działania: {gx(4,5):.3f}")

ms = Miasto(45,"Lublin","lubelelskie")
ms.print_miasto()
