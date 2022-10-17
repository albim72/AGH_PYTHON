#opiszemy konstrukcję Switch - case, gdzie Switch będzie klasą reprezentującą przekazaną do warunku wartość
# case będzie funkcją przetwarzającą przekazaną wartość według listy przypadków

class Switch:
  
    value = None
    def __new__(cls, value):
        cls.value=value
        return True
    
def case(*args):
    return any((arg == Switch.value for arg in args))
