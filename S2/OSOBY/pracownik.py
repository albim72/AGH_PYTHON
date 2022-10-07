from osoba import Osoba

class Pracownik(Osoba):
    
    #konstruktor z dziedziczeniem
    def __init__(self,imie,wiek,wzrost,waga,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie,wiek,wzrost,waga)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie
        
    def print_pracownik(self):
        print(f"dane pracownika -> firma: {self.firma}, stanowisko: {self.stanowisko}, lata pracy: {self.latapracy}, "
              f"wynagrodzenie: {self.wynagrodzenie} zł.")

    def czypracownik(self):
        return True
