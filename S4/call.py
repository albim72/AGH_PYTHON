class Miasto:

    def __init__(self):
        print("utworzono nową instancję klasy Miasto")

    def __call__(self,nazwa):
        print("instancja klasy zostałą wywołana przez funckję magiczną  __call__\n"
              f"nazwa miasta: {nazwa}")

vb = Miasto()
vb("Toruń")
