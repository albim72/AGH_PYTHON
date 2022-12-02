from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    
    @abstractmethod
    def useful_function_a(self)->str:
        pass
    
