'''
2. iz prethodne vjezbe iskoristite klasu zivotinja: iz nje izvedite 3 klase (mesojedi, biljojedi, svejedi). 
iz svake od navedenih klasa izvedite po jednu klasu sa nazivom zivotinje (npr slon, sova, riba). 
osmislite atribute i metode tako da budu smisleni i neka nesto ispisuju - npr. iz klase mesojed, neka ispise: "hranim se mesom!".
'''

class Zivotinja:
    def __init__(self, naziv, masa):
        self.naziv = naziv
        self.masa = masa

    def ispisi_naziv(self):
        print(f"Zovem se {self.naziv}")

    def ispisi_tezinu(self):
        print(f"Težak sam {self.masa} kg")


class Mesojed(Zivotinja):
    def __init__(self, naziv, masa, ishrana):
        super().__init__(naziv, masa)
        self.ishrana = ishrana

    def ispisi_ishranu(self):
        print(f"Hranim se {self.ishrana}")

    
class Biljojed(Zivotinja):
    def __init__(self, naziv, masa, ishrana):
        super().__init__(naziv, masa)
        self.ishrana = ishrana

    def ispisi_ishranu(self):
        print(f"Hranim se {self.ishrana}")


class Svejed(Zivotinja):
    def __init__(self, naziv, masa, ishrana):
        super().__init__(naziv, masa)
        self.ishrana = ishrana

    def ispisi_ishranu(self):
        print(f"Hranim se {self.ishrana}")


class Tigar(Mesojed):
    def __init__(self, naziv, masa, ishrana):
        super().__init__(naziv, masa, ishrana)


class Slon(Biljojed):
    def __init__(self, naziv, masa, ishrana):
        super().__init__(naziv, masa, ishrana)


class Svinja(Svejed):
    def __init__(self, naziv, masa, ishrana):
        super().__init__(naziv, masa, ishrana)


tigar1 = Tigar("Tigar", 80, 'meso')
tigar1.ispisi_ishranu()
tigar1.ispisi_naziv()
tigar1.ispisi_tezinu()