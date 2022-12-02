from abc import ABC, abstractmethod
from abstract_a import AbstractProductA

class AbstractProductB(ABC):
    
    @abstractmethod
    def useful_function_b(self)->str:
        pass
    
    @abstractmethod
    def another_useful_function_b(self,collaborator:AbstractProductA)->None:
        pass
