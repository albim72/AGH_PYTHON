class Kolor:

    #opis stanu - konstruktor klasy
    def __init__(self,id,nazwa):
        self.idkoloru = id
        self.nazwa = nazwa
        self.paleta = "paleta X"

    #opis zachowania -> funkcje klasy(metody)
    def print_kolor(self):
        print(f"Kolor -> id: {self.idkoloru}, nazwa: {self.nazwa}, paleta: {self.paleta}")


k1 = Kolor(2,"czarny")
k2 = Kolor(24,"czerwony")

k1.print_kolor()
k2.paleta = "paleta A"
k2.print_kolor()

k3 = Kolor(101,"Navy")
k3.print_kolor()
