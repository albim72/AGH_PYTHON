from abstract import AbstractProductA

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) ->str:
        return "wynik: produkt A1"
    
class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) ->str:
        return "wynik: produkt A2"
