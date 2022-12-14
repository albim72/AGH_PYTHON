class PierwszaKlasa:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def print_ab(self):
        print(f"a = {self.a}, b = {self.b}")


class DrugaKlasa(PierwszaKlasa):

    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c

    def print_abc(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")

    def suma_elementow(self):
        return self.a + self.b + self.c


class SpecjalnaKlasa:

    def __init__(self,g,h):
        self.g = 2*g
        self.h = h**2

    def ghx(self):
        return (self.g+self.h)/2

class TrzeciaKlasa(DrugaKlasa,SpecjalnaKlasa):

    def __init__(self,a,b,c,d,g,h):
        DrugaKlasa.__init__(self,a,b,c)
        SpecjalnaKlasa.__init__(self,g,h)
        self.d=d

    def print_abcdgh(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}, d={self.d}, g={self.g}, h={self.h}")

    def suma_elementow(self):
        return self.a + self.b + self.c + self.d + self.ghx()

pk = PierwszaKlasa(3,7)
dk = DrugaKlasa(1,6,9)
tk=TrzeciaKlasa(2,3,1,8,2,3)

print("___________ PierwszaKlasa __________")
pk.print_ab()
print("___________ DrugaKlasa __________")
dk.print_ab()
dk.print_abc()
print(dk.suma_elementow())
print("___________ TrzeciaKlasa __________")
tk.print_ab()
tk.print_abc()
tk.print_abcdgh()
print(tk.suma_elementow())



