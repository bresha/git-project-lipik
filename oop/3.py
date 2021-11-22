'''
3. napravite klasu Geometrijski_lik. 
klasa treba imati mogucnost proracuna oplosja i obujma kugle, 
valjka i kvadra te ispis navedenih oplosja te koristenih formula za proracun. 
ispisite na ekran sve navedeno.
'''
import math


class Geometrijski_lik:
    def __init__(self, tijelo, x, h=0):
        self.tijelo = tijelo
        self.x = x
        self.h = h

    def izracunaj_oplosje(self):
        oplosje = 0
        if self.tijelo == 'kugla':
            oplosje = 4 * math.pi * self.x**2
        if self.tijelo == 'valjak':
            oplosje = 2 * math.pi * self.x * (self.x + self.h)
        if self.tijelo == 'kvadar':
            oplosje = 2 * self.x**2 + 4 * self.x * self.h
        print(oplosje)

    def izracunaj_volumen(self):
        volumen = 0
        if self.tijelo == 'kugla':
            volumen = 4/3 * math.pi * self.x**3
        if self.tijelo == 'valjak':
            volumen = math.pi * self.x**2 * self.h
        if self.tijelo == 'kvadar':
            volumen = self.x**2 * self.h
        print(volumen)


kugla = Geometrijski_lik('kugla', 12)
kugla.izracunaj_oplosje()
kugla.izracunaj_volumen()

valjak = Geometrijski_lik('valjak', 2, 5)
valjak.izracunaj_oplosje()
valjak.izracunaj_volumen()

kvadar = Geometrijski_lik('kvadar', 4, 3)
kvadar.izracunaj_oplosje()
kvadar.izracunaj_volumen()