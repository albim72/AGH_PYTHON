class Sport:

    def __init__(self,dyscyplina,lata_upr,best_wynik):
        self.dysycyplina = dyscyplina
        self.lata_upr = lata_upr
        self.best_wynik = best_wynik

    def infosport(self):
        print(f"Dysycyplina: {self.dysycyplina}, lata uprawiania: {self.lata_upr}, życiówka: {self.best_wynik}")
