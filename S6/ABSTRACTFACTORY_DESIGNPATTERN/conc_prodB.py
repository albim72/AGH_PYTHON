from abstract_a import AbstractProductA
from abstract_b import AbstractProductB

class ConcreteProductB1(AbstractProductB):

    def useful_function_b(self) ->str:
        return "wynik: produkt B1"

    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        result = collaborator.useful_function_a()
        return f"wynik dla B1 połączony z {result}"

class ConcreteProductB2(AbstractProductB):

    def useful_function_b(self) ->str:
        return "wynik: produkt B2"

    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        result = collaborator.useful_function_a()
        return f"wynik dla B2 połączony z {result}"

