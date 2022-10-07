class Miasto:

    def __init__(self,id,nazwa,woj):
        self.id = id
        self.nazwa = nazwa
        self.woj = woj

    def print_miasto(self):
        print(f"Miasto {self.nazwa}, id: {self.id}, województwo: {self.woj}")
