from pracownik import Pracownik
from sport import Sport
from empty import Pusta

class Student(Pracownik,Sport,Pusta):

    #konstruktor z wielodziedziczeniem
    def __init__(self,imie,wiek,wzrost,waga,nr_studenta,wydzial,kierunek,rok_stud,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dyscyplina="",lata_upr="",best_wynik=""):
        Pracownik.__init__(self,imie,wiek,wzrost,waga,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lata_upr,best_wynik)
        self.nr_studenta = nr_studenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rok_stud = rok_stud


    def print_student(self):
        print(f"dane studenta nr {self.nr_studenta} -> wydział: {self.wydzial}, kierunek: {self.kierunek}, "
              f"rok studiów: {self.rok_stud}")

    def czypracownik(self):
        return self.firma != ""
