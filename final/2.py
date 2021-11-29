'''
2. u klasi iz prethodnog zadatka napravi "pseudo lutriju" 6/39, 
odnosno program koji bi od 0-39 brojeva uzeo nasumicnih 6 (bez ponavljanja) 
i trazio od korisnika unos brojeva. 
kada korisnik unese tih 6 brojeva, 
treba ispisati koliko brojeva je korisnik pogodio i njegov postotak tocnosti 
(npr. ako je pogodio 3 broja, treba ispisati 50%). 
nadogradite program tako da prima varijable umjesto brojeva 39 i 6 
i neka se korisnika pita za unos istih (npr. 52 i 3, odnosno 3/52).
'''

from random import randint

class Lutrija:
    def __init__(self) -> None:
        self.sveukupno_brojeva = int(input("Do kojeg broja se izvlaci?: "))
        self.sveukupno_izvlacenja = int(input("Koliko brojeva se izvlaci?: "))
        self.brojevi = list(range(1, self.sveukupno_brojeva + 1))
        self.brojevi_korisnika = list()

    def izvuci_brojeve(self):
        self.izvuceni_brojevi = list()
        for _ in range(self.sveukupno_izvlacenja):
            index = randint(0, len(self.brojevi))
            broj = self.brojevi.pop(index)
            self.izvuceni_brojevi.append(broj)
        print(self.izvuceni_brojevi)
        
    def unesi_brojeve(self):
        while len(self.brojevi_korisnika) != self.sveukupno_izvlacenja:
            broj = int(input("Unesi broj: "))
            if broj not in self.brojevi_korisnika and broj in range(0, self.sveukupno_brojeva + 1):
                self.brojevi_korisnika.append(broj)
            else:
                print("Ne mozete unijeti taj broj!")
        print(self.brojevi_korisnika)

    def izracunaj_postotak(self):
        broj_pogodaka = 0
        for number in self.brojevi_korisnika:
            if number in self.izvuceni_brojevi:
                broj_pogodaka += 1
        postotak = round(broj_pogodaka / self.sveukupno_izvlacenja * 100, 2)
        print(f"Pogodili ste {postotak}%")

    def start(self):
        self.unesi_brojeve()
        self.izvuci_brojeve()
        self.izracunaj_postotak()

if __name__ == '__main__':
    lutrija = Lutrija()
    lutrija.start()