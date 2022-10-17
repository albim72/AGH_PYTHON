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


#przykład 2

def gratulacje(jesli):
    def gratuluj(nr_pod):
        return f"Garatulacje zdanego egzaminu! podejścia nr: {nr_pod}"
    def szkoda():
        return "Przykro! Następnym razem będzie lepiej..."
    def inne():
        return "podaj tak lub nie"
    
    if jesli == "tak":
        return gratuluj
    elif jesli == "nie":
        return szkoda
    else:
        return inne


print(gratulacje("tak")(2))
print(gratulacje("nie")())
print(gratulacje("aaaaaa")())
