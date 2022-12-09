import threading

def print_square(liczba):
    print(f"kwadrat liczby {liczba} wynosi {liczba**2}")

def print_cube(liczba):
    print(f"sześcian liczby {liczba} wynosi {liczba**3}")

if __name__ == '__main__':
    t1 = threading.Thread(target=print_square,args=(10,))
    t2 = threading.Thread(target=print_cube,args=(10,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Wykonano!")
