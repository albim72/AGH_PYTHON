from osoba import Osoba

os1 = Osoba("Jan",66,176,104)
os1.print_osoba()
print(f"wiek za 10 lat: {os1.wiekza10lat()}")
print(f"Czy osoba jest pracownikiem? ({os1.czypracownik()})")
