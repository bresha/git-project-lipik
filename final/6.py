'''
6. napravite klasu za upravljanje nuklearnog reaktora. da bi nuklearni reaktor radio, mora biti u nekakvom stanju kriticnosti. 
ako je manji od tog stanja, onda moze biti ostecen. ako je iznad tog stanja, onda moze uzrokovati katastrofu i meltdown. 
kriticnost je zadovoljena ako je temperatura manja od 800, broj emitiranih neutrona po sekundi je veci od 500 i umnozak temperature i emitiranih neutrona po sekundi manji od 500.000.
'''


class Reaktor:
    def __init__(self, temp, neutroni_po_sek) -> None:
        self.temp = temp
        self.neutroni_po_sek = neutroni_po_sek

    def provjeri_kriticnost(self):
        if self.temp < 800 and self.neutroni_po_sek > 500 and (self.temp * self.neutroni_po_sek) < 500000:
            print("Kriticnost zadovoljena!")
        else:
            print("Meltdown ili ostecenje")