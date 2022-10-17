#przykład 1

def pozdrowienie(name):
    return f"Miło Cię widzieć: {name}"

def konferencja(name):
    return f"Prelegent: {name}"

#funkcja osoba to funkcja wyższego rzędu - funkcja której parametrem jest inna funkcje
def osoba(funkcja,name):
    return funkcja(name)

print(osoba(pozdrowienie,"Leon"))
print(osoba(konferencja,"Karol"))
