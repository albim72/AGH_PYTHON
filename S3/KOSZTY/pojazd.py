from ipojzad import IPojazd

class Pojazd(IPojazd):

    def spalanie_100(self, litry, odl):
        return litry*100/odl

    def kosztyprzejazdu(self, litry, odl, cena_l):
        return self.spalanie_100(litry,odl)*(odl/100)*cena_l
