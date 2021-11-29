'''
1. napravite klasu za pogadjanje brojeva. program treba odrediti random interval brojeva [-random, random] 
te iz njega uzeti broj koji se nalazi u sredini (postavi granice randoma za granice intervala na 1000). 
traziti unos od korisnika da unese broj koji je program odredio. ako se broj nalazi u intervalu, 
program treba ispisati: "toplo", ako je njegov iduci unos blizi broju koji se od njega trazi, treba ispisati: "toplije", 
a ako unese broj koji se nalazi izvan intervala, treba ispisati poruku: "hladno". 
ispisite i broj koraka koje je korisnik trebao napraviti da bi dosao do rjesenja.

'''

import random

class PogađanjeBrojeva:
    def __init__(self) -> None:
        self.interval = range(0 , random.randint(0, 1000))
        self.sredina = self.interval[round(len(self.interval)/2)]
        self.prosli_odabir = None
        self.broj_koraka = 0

    def gadjaj(self):
        odabir = int(input("Pogodi broj: "))
        print('interval', self.interval)
        print('sredina', self.sredina)
        self.broj_koraka += 1
        if odabir == self.sredina:
            return 'pogodjeno'
        if self.prosli_odabir == None:
            if odabir in self.interval:
                self.prosli_odabir = odabir
                return 'toplo'
            else:
                return 'hladno'
        else:
            novi_interval = self.izracunaj_novi_interval()
            print(novi_interval)
            if odabir in novi_interval:
                self.prosli_odabir = odabir
                return 'toplije'
            else:
                self.prosli_odabir = odabir
                return 'hladnije'

    def izracunaj_novi_interval(self):
        razlika = abs(self.sredina - self.prosli_odabir)
        donji = self.sredina - razlika
        gornji = self.sredina + razlika + 1
        return range(donji, gornji)

    def run(self):
        while True:
            rezultat = self.gadjaj()
            if rezultat == 'pogodjeno':
                print(rezultat)
                break
            else:
                print(rezultat)


if __name__ == '__main__':
    pogadjalo = PogađanjeBrojeva()
    pogadjalo.run()
