from osoba import Osoba
from pracownik import Pracownik
from student import Student

os1 = Osoba("Jan",66,176,104)
os1.print_osoba()
print(f"wiek za 10 lat: {os1.wiekza10lat()}")
print(f"Czy osoba jest pracownikiem? ({os1.czypracownik()})")
print(f"współczynnik bmi wynosi: {os1.bmi():.2f}, opis: {os1.opis_bmi()}")

print("___________________________________________________")

os2 = Osoba("Olga",26,170,62)
os2.koloroczu = "niebieskie"
os2.print_osoba()
print(f"wiek za 10 lat: {os2.wiekza10lat()}")
print(f"Czy osoba jest pracownikiem? ({os2.czypracownik()})")

print("___________________________________________________")

pr1 = Pracownik("Karol",42,173,108,"ABC sp zoo","dyrektor",12,10900)
pr1.print_osoba()
pr1.print_pracownik()
print(f"wiek za 10 lat: {pr1.wiekza10lat()}")
print(f"Czy osoba jest pracownikiem? ({pr1.czypracownik()})")
print(f"współczynnik bmi wynosi: {pr1.bmi():.2f}, opis: {pr1.opis_bmi()}")

print("___________________________________________________")

st1 = Student("Olaf",22,177,77,756545,"Automatyki, Elektroniki i Informatyki","Informatyka",3)

st1.print_osoba()
st1.print_student()
print(f"wiek za 10 lat: {st1.wiekza10lat()}")
print(f"Czy osoba jest pracownikiem? ({st1.czypracownik()})")

print("___________________________________________________")

st2 = Student("Anna",23,170,58,987777,"Nauk Społecznych","Socjologia",4,"XYZ","sekretarka",1,2400)

st2.print_osoba()
st2.print_student()
st2.print_pracownik()
print(f"wiek za 10 lat: {st2.wiekza10lat()}")
print(f"Czy osoba jest pracownikiem? ({st2.czypracownik()})")

#stwórz obiekt st3 klasy Student, który nie jest pracowmnikiem ale jest sportowcem

print("___________________________________________________")

st3 = Student("Robert",22,178,80,323424,"Budowlany","Budowa i konstrukcja mostów",3,dyscyplina="biegi ultra",
              lata_upr=5, best_wynik="102km 18godz 56min 23s")

st3.print_osoba()
st3.print_student()
st3.infosport()
print(f"wiek za 10 lat: {st3.wiekza10lat()}")
print(f"Czy osoba jest pracownikiem? ({st3.czypracownik()})")
print(f"współczynnik bmi wynosi: {st3.bmi():.2f}, opis: {st3.opis_bmi()}")


