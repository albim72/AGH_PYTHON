liczby = [78,34,1,-55,0,213,45667,-6664,345,112,99,2,1009,222,-999]

def pokaz_stat(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    return minimum,maksimum,rozstep

wynik = pokaz_stat(liczby)
print(wynik)

mini, maxi, roz = pokaz_stat(liczby)
print(f'wartość maksymalna: {maxi}, wartość minimalna: {mini}, rozstęp: {roz}')
