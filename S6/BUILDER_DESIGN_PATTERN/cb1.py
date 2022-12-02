from builder import Builder
from pod1 import Product1

class ConcreteBuilder1(Builder):

    def __init__(self)->None:
        self.reset()
        
    def reset(self):
        self._product = Product1()
        
    @property
    def product(self) ->Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")
    
    
