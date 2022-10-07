nazwa_classic = ['samolot','marchewka','miecz','mecz','Mieczysław','Romuald','piorun','macierz',
                 'miecznik','123','atak','zenit','Łódź','Ącka']

def low_sign(lista):
    for i,w in enumerate(lista):
        lista[i] = w.lower()
    return lista


def bsort_classic(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i].lower() < a[i-1].lower():
                temp = a[i]
                a[i] =a[i-1]
                a[i-1] = temp

#print(low_sign(nazwa_classic))

bsort_classic(nazwa_classic)
print(nazwa_classic)

nazwa_modern = ['samolot','marchewka','miecz','mecz','Mieczysław','Romuald','piorun','macierz',
                 'miecznik','123','atak','zenit','Łódź','Ącka']


def bsort_modern(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i].lower() < a[i-1].lower():
                a[i-1],a[i] = a[i],a[i-1]

bsort_modern(nazwa_modern)
print(nazwa_modern)
