class Pracownik:

    def __init__(self):
        print("pracownik został utworzony")

    def info(self):
        print("pracownik firmy ABC...")

    def __del__(self):
        print("destruktor wywołany, pracownik usunięty!")


prac = Pracownik()
prac.info()
prac.info()
prac.info()
del prac

print("czy program działa dalej?")
# prac.info()

def tworzenie_pracownika():
    print("Utworzenie nowego pracownika.....")
    print("Pracownik został utworzony....")
    return Pracownik()


np = tworzenie_pracownika()
np.info()
del np

# np.info()

