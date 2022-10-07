from osoba import Osoba

os1 = Osoba("Jan",66,176,104)
os1.print_osoba()
print(f"wiek za 10 lat: {os1.wiekza10lat()}")
print(f"Czy osoba jest pracownikiem? ({os1.czypracownik()})")

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
