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
    
    
class TrzeciaKlasa(DrugaKlasa):

    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d
        
    def print_abcd(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}, d={self.d}")

    def suma_elementow(self):
        return self.a + self.b + self.c + self.d
