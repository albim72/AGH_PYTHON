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
