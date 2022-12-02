from abc import ABC,abstractmethod
from abstract_a import AbstractProductA
from abstract_b import AbstractProductB

class AbstractFactory(ABC):
    
    @abstractmethod
    def create_product_a(self)->AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
    
