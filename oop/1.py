'''
1. napravite klasu Zivotinja. 
unutar klase definirajte konstruktor koji sadrzi atribute za naziv, tip, masu, vrstu ishrane. 
definirajte i metodu unutar klase koja ce ispisati navedene atribute. 
u glavnom potprogramu kreirajte dva razlicita objekta te pozovite kreiranu metodu.
'''

class Zivotinja:
    def __init__(self, naziv, tip, masa, ishrana):
        self.naziv = naziv
        self.tip = tip
        self.masa = masa
        self.ishrana = ishrana

    def isprintaj(self):
        print(self.naziv, self.tip, self.masa, self.ishrana)

pas = Zivotinja("Rex", "pas", "15kg", "pseća hrana")
macka = Zivotinja("Mica maca", "mačka", "5kg", "mačja hrana")

pas.isprintaj()
macka.isprintaj()