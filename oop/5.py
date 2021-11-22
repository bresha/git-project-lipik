'''
5. napravite klasu Banka. definirajte atribute korisnika u obliku rjecnika (oib, ime, prezime, stanje racuna, mjesecni prihod, ima li osiguranje). 
napravite metodu za podizanje kredita. 
metoda mora provjeriti da li je stanje racuna pozitivno, jesu li mjesecni prihodi visi od 5% od ukupne trazene svote kredite. ukoliko jesu, metoda vraca True. 
napravite metodu koja bi izracunala koliko bi mjeseci (i godina) bilo potrebno da korisnik vrati novac. 
nadogradite program tako da racuna i kamate na godisnjoj razini te ispisite rezultat.
'''
import math


class Banka:
    def __init__(self, oib, ime, prezime, stanje_racuna, mjesecni_prihod, osiguranje):
        self.korisnik = dict()
        self.korisnik['oib'] = oib
        self.korisnik['ime'] = ime
        self.korisnik['prezime'] = prezime
        self.korisnik['stanje_racuna'] = stanje_racuna
        self.korisnik['mjesecni_prihod'] = mjesecni_prihod
        self.korisnik['osiguranje'] = osiguranje

    def kreditna_sposobnost(self, iznos_kredita):
        if self.korisnik['stanje_racuna'] > 0 and self.korisnik['mjesecni_prihodi'] > (iznos_kredita * 0.05):
            return True
        return False

    def duzina_vracanja(self, iznos):
        mjeseci = iznos / (self.korisnik['mjesecni_prihod'] * 0.33)
        godine = mjeseci // 12
        mjeseci = mjeseci - godine * 12
        print(f"Za vracanje kredita potrebno je {godine} godina i {math.ceil(mjeseci)} mjeseci")
        return godine, mjeseci

    def izracunaj_kamate(self, iznos, eks):
        godine, mjeseci = self.duzina_vracanja(iznos)
        return eks * 1 / godine * iznos



b = Banka('22343532', 'Pero', 'Peric', 10000, 5000, True)
b.duzina_vracanja(100000)
print(b.izracunaj_kamate(100000, 10))

        