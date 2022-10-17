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

#przypadek 2

def sleep(funkcja):
    def wrapper():
        time.sleep(8)
        return funkcja()
    return wrapper

@sleep
def info():
    print("komunikat po 8 sekunadach!")

info()

@sleep
@pomiarczasu_
def suma_z_listy():
    sum([i**2 for i in range(1000000)])

suma_z_listy()


#przypadek 3

def debug(funkcja):
    def wrapper():
        print(f"wywołanie funkcji: {funkcja.__name__}")
    return wrapper

@debug
def takietam(r):
    return r

takietam(3)


#przypadek 4
def repeat(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeat(n=5)
def policz(c,d):
    print(f"wartość = {c*d**2}")

policz(3,6)
