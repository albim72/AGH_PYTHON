from builder import Builder
from director import Director
from cb1 import ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("Podstawowy produkt")
director.build_minimal_variable_product()
builder.product.list_parts()

print("\n")

print("Pełny produkt:")
director.build_full_featured_product()
builder.product.list_parts()

print("\n")

print("Produkt - wersja użytkownika:")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()

print("\n")
