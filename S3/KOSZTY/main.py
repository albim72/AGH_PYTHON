from pojazd import Pojazd

p1 = Pojazd()
lt = float(input("podaj liczbę spalonych litrów paliwa: "))
odl = float(input("podaj przejechaną odległość: "))
cena_l = float(input("poda cenę za l paliwa: "))
print(f"spalanie [l/100km]: {p1.spalanie_100(lt,odl):.2f}")
print(f"koszt przejazdu na trasie: {odl}km wynosi: {p1.kosztyprzejazdu(lt,odl,cena_l):.2f} zł")
