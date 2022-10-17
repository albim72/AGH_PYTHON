def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("Dzielenie przez 0!")
    except NameError:
        print("brak zmiennej!")
    except TypeError:
        print("nie można dzielić tekstu przez liczbę")
    else:
        print(f'wynik dzielenia: {wynik}')
    finally:
        print('policzmy coś jeszcze')
        print("___________________________________")

try:
    dzielenie(5,6)
    dzielenie(0,6)
    dzielenie(9,0)
    dzielenie(12,0.0005343354)
    dzielenie(67,True)
    dzielenie(-3.678, 0.0000000000006)
    dzielenie("hhhhhh",34)
    dzielenie(7)
except TypeError:
    print("podaj właściwa liczbę argumentów")
