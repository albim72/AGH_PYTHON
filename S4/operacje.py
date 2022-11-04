def dodawanie(self,x,y):
    return x+y

def odejmowanie(self,x,y):
    return x-y

def mnozenie(self,x,y):
    return x*y


class Dzialanie(type):
    def __init__(cls,clsname,bases,attrs):
        if clsname == "Dodaj":
            cls.operacja = dodawanie
        elif clsname == "Odejmij":
            cls.operacja = odejmowanie
        elif clsname == "Pomnoz":
            cls.operacja = mnozenie
        else:
            return "zły wybór!"

class Dodaj(metaclass=Dzialanie):
    pass
class Odejmij(metaclass=Dzialanie):
    pass
class Pomnoz(metaclass=Dzialanie):
    pass


op1 = Dodaj()
print(f"wynik działania a+b = {op1.operacja(5,6)}")
op2 = Odejmij()
print(f"wynik działania a-b = {op2.operacja(5,6)}")
op3 = Pomnoz()
print(f"wynik działania a*b = {op3.operacja(5,6)}")



