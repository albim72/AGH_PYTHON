class Kolor:
    def __init__(self,numer):
        self.numer = numer

    def __getattr__(self, name):
        return f'Kolor nie posiada atrybutu: {name}'

kl = Kolor("numer")

print(kl.numb)
print(kl.numer)
