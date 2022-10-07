class Osoba:

    def __init__(self,imie,wiek,wzrost,waga):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.waga = waga
        self.koloroczu = "brązowe"
        self.info()

    def info(self):
        print("tworzenie nowej osoby....")

    def print_osoba(self):
        print(f"Osoba -> imię: {self.imie}, wiek: {self.wiek} lat/a, wzrost: {self.wzrost} cm, "
              f"waga: {self.waga} kg, kolor oczu: {self.koloroczu}")

    def wiekza10lat(self):
        return self.wiek + 10

    def czypracownik(self):
        return False
