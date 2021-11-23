'''
4. klasu Geometrijski_lik iz prethodne vjezbe preuredite tako da se iz nje izvode klase za kuglu i valjak. 
definirajte prikladne metode i atribute za pojedinu klasu. 
neka u nadklasi (super klasi) bude definiran samo onaj atribut koji se ponavlja u podklasama
'''
import math

class GeometrijskiLik:
    def __init__(self, r):
        self.r = r

    def oplosje():
        pass

    def obujam():
        pass

class Kugla(GeometrijskiLik):
    def __init__(self, r):
        super().__init__(r)
    
    def oplosje(self):
        return 4 * math.pi * self.r**2

    def obujam(self):
        return 4/3 * math.pi * self.r**3

class Valjak(GeometrijskiLik):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def oplosje(self):
        return 2 * math.pi * self.r * (self.r + self.h)

    def obujam(self):
        return math.pi * self.r**2 * self.h

kugla = Kugla(12)

print(kugla.obujam(), kugla.oplosje())

valjak = Valjak(12, 12)

print(valjak.obujam(), valjak.oplosje())
