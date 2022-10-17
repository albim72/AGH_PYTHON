from abc import ABC, abstractmethod

class Prototyp(ABC):
    
    def __init__(self,x):
        self.x = x
        
    def info(self):
        print("to jest metoda nieabstrakcyjna klasy abstrakcyjnej")
        
    @abstractmethod
    def policz(self):
        pass
    
    @abstractmethod
    def policz_x(self):
        return self.x*5
    
    
class ZwKlasa(Prototyp):

    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 7008

    def policz_x(self):
        return super().policz_x() + 4*self.y

    def message(self,i):
        return f"ważna wiadomość: {i}"


z = ZwKlasa(4,3)

z.info()
print(z.message("kod -> 96789634859834"))
print(f"wynik zwracany przez metodę policz -> {z.policz()}")
print(f"wynik zwracany przez metodę policz_x -> {z.policz_x()}")
