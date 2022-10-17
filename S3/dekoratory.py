import time

def pomiarczasu_(funkcja):
    def wrapper():
        #perf_counter -> czas od granicy czasowej
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f"czas wykonania funckji: {endtime - starttime} s")
    return wrapper

def pomiarczasu_lista(funkcja):
    def wrapper(lista):
        #perf_counter -> czas od granicy czasowej
        starttime = time.perf_counter()
        funkcja(lista)
        endtime = time.perf_counter()
        print(f"czas wykonania funckji: {endtime - starttime} s")
    return wrapper


#w obu przypadkach funkcje mierzą czas od granicy czasowej [s]
print(time.perf_counter()) #czas od momentu uruchomienia funkcji print
print(time.time()) #czas który upłynął do epoki do uruchomienia funkcji print

@pomiarczasu_
def suma_z_listy():
    sum([i**2 for i in range(1000000)])

suma_z_listy()

lt = [i**2 for i in range(1000000)]
lt2 = [4,5,67,89,5]
@pomiarczasu_lista
def suma_z_listy_2(lista):
    sum(lista)

suma_z_listy_2(lt)
