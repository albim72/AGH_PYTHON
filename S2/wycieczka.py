# def kwota(transport,nocleg_wyzywienie,wycieczki,ubezpieczenie,inne,rabat)
# -> (transport+nocleg_wyzywienie)*(1-rabat/100)+wycieczki+ubezpieczenie+inne

#dostępny rabat tylko w zakresie od 0 do 70 %
#rabat = 0 domyślny

def kwota(t,nw,w,u,i,rab=0):
    if rab>=0 and rab <= 70:
        return (nw+t)*(1-rab/100)+w+u+i
    else:
        return "podaj rabat mniejszy niż 70% lub większy od 0"

print(f"{kwota(100,100,50,50,50):.2f} zł")
print(f"{kwota(100,100,50,50,50,25):.2f} zł")
print(f"{kwota(100,100,50,50,50,75)} zł")

wynik = []
for r in rabs:
    kw = kwota (1700, 1230, 450, 200, 180, r)

    if r == 0:
        print (f"cena bazowa do zapłaty wynosi: {kw} zł")

    else:
        print (f"dla rabatu: {r}%, kwota do zapłaty wynosi: {kw} zł")

    wynik.append(kw)


print (wynik)

result = [kwota(1700,1230,450,200,180,r) for r in rabs]
print(result)
