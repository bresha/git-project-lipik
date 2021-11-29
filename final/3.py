'''
3. zapisite intervale, brojeve, pogadjanja i postotke tocnosti u zasebne datoteke (imenujte ih po zelji). 
neka izgled unutar datoteke bude zapisan na sljedeci nacin: 
	a) za prvi zadatak --> [min, max] | uneseni_brojevi[broj1, broj2, broj3, ...] | broj_koraka
	b) za drugi zadatak --> 6/39 | uneseni_brojevi[broj1, broj1, broj3, ...] | postotak_pogodaka
'''
from random import shuffle
import os


class Lutrija:
    def __init__(self) -> None:
        self.sveukupno_brojeva = int(input("Do kojeg broja se izvlaci?: "))
        self.sveukupno_izvlacenja = int(input("Koliko brojeva se izvlaci?: "))
        self.brojevi_korisnika = list()
        self.unesi_brojeve()

    def izvuci_brojeve(self):
        self.izvuceni_brojevi = list()
        brojevi = list(range(1, self.sveukupno_brojeva + 1))
        shuffle(brojevi)
        for _ in range(self.sveukupno_izvlacenja):
            broj = brojevi.pop()
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
        self.postotak = round(broj_pogodaka / self.sveukupno_izvlacenja * 100, 2)
        print(f"Pogodili ste {self.postotak}%")

    def start(self):
        self.izvuci_brojeve()
        self.izracunaj_postotak()
        
    def sazetak(self):
        return f'{self.sveukupno_izvlacenja}/{self.sveukupno_brojeva}|{self.postotak}'


def main():
    lutrija = Lutrija()
    broj_kola = int(input("Unesite koliko kola zelite odigrati: "))
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'lutrija.txt')
    with open(file_path, 'w', encoding='utf-8') as f:
        for _ in range(broj_kola):
            lutrija.start() 
            sazetak = lutrija.sazetak()
            f.write(sazetak + '\n')

if __name__ == '__main__':
    main()
