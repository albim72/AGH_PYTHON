class Kwadrat:

    def __init__(self,bok):
        self.bok = bok

    def pole(self):
        return self.bok**2


class Prostokat:

    def __new__(cls, szer:float, wys:float):
        if szer == wys:
            return Kwadrat(bok=szer)
        return object.__new__(Prostokat)

    def __init__(self,szer:float, wys:float):
        self.szer = szer
        self.wys = wys

    def pole(self):
        return self.szer*self.wys


r1 = Prostokat(5,9)
r2 = Prostokat(4,4)
print(f"pole figury: {r1.__class__.__name__} -> {r1.pole()}")
print(f"pole figury: {r2.__class__.__name__} -> {r2.pole()}")
print(type(r1))
print(type(r2))
