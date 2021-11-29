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
        self.interval = range(-random.randint(0, 1000), random.randint(0, 1000))
        self.sredina = round(self.interval[len(self.interval)/2])
        self.prosli_pogodak = None

