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
       
        
    def bmi(self):
        return self.waga/(self.wzrost/100)**2

    def opis_bmi(self):
        if self.bmi() < 18.5:
            return "niedowaga"
        elif self.bmi() <= 25:
            return "waga prawidłowa"
        elif self.bmi() <= 30:
            return "nadwaga"
        else:
            return "otyłość"
        
    def policz_ppm(self,plec):
        if plec == "k":
            return 655.1 + 9.563*self.waga+1.85*self.wzrost-4.676*self.wiek
        elif plec == "m":
            return 66.5 + 13.75 * self.waga + 5.003 * self.wzrost - 6.775 * self.wiek
        else:
            return "podaj k lub m"
