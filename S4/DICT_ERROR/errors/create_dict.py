class IntFloatValueError(Exception):

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f'{self.value} jest niewłaściwą wartością. ' \
               f'Słownik może zawierać tylko wartości typu: int i float'


class KeyValueContructError(Exception):

    def __init__(self, key, value):
        self.key = key
        self.value = value


    def __str__(self):
        return f'klucze i wartości mogą pochodzić tylko z kolekcji: list albo tuple.' \
               f'Aktualnie klucz posiada wartość: {self.key} w typie {type(self.key)}, ' \
               f'a wartość słownika posiada wartość: {self.value} w typie {type(self.value)}'
