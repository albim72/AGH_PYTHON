from prostokat import Prostokat
from trojkat import Trojkat
from trapez import Trapez
from kolo import Kolo

pr = Prostokat(5.5,7.3)
tr = Trojkat(6.7,9)
trp = Trapez(8.2,6.3,4.8)
kl = Kolo(5.5)

print(f"pole prostokąta wynosi: {pr.policz_pole():.2f}")
print(f"pole trójkąta wynosi: {tr.policz_pole():.2f}")
print(f"pole trapezu wynosi: {trp.policz_pole():.2f}")
print(f"pole Koła wynosi: {kl.policz_pole():.2f}")
