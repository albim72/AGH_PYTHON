#definicja własnej klasy błędu

class MojBlad(Exception):

    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("wołanie konstruktora __str__")
        if self.message:
            return f"MojBlad {self.message}"
        else:
            return f"MojBlad został użyty"

raise MojBlad("Mamy specjalny problem .... ")
