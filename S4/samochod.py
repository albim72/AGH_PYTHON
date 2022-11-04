class Samochod:

    def __init__(self,marka,model,rocznik,cena,rata):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.cena = cena
        self.rata = rata


    @staticmethod
    def salon(miasto):
        return f"miasto salonu sprzedaży: {miasto}"

    @classmethod
    def obliczenie_raty(cls,cena,miesiac):
        return cls("Opel","Insignia",2019,56788,1.3*cena/miesiac)

sm = Samochod("Jeep","Cherokee",2020,120000,1278)
sm2 = Samochod.obliczenie_raty(57800,48)

print(sm.salon("Toruń"))
print(sm.rata)
m1 = sm2.salon("Kraków")
print(m1)
print(sm2.rata)
