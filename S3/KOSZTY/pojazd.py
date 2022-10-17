from ipojzad import IPojazd
from imarka import IMarka


class Pojazd(IPojazd,IMarka):

    def __init__(self,marka,model,rocznik,poj):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.poj = poj

    def spalanie_100(self, litry, odl):
        return litry*100/odl

    def kosztyprzejazdu(self, litry, odl, cena_l):
        return self.spalanie_100(litry,odl)*(odl/100)*cena_l

    def info_car(self):
        return f"Opis pojazdu: {self.marka}, model: {self.model}, rok produkcji: {self.rocznik}, pojemność: {self.poj}"

