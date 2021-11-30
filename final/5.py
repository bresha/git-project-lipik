'''
5. napravite klasu za igru s rijecima. unutar klase napravite metode koje imaju sljedece funkcionalnosti:
	a) od unesene recenice (min 3 rijeci, ponoviti unos ako uvjet nije zadovoljen) neka generira akronim (skracenicu). 
    npr. "I Love Cats" -> "ILC". nadogradite ju tako da akronim ima max 3 slova i to od najvecih rijeci
	b) metodu koja prebrojava rijeci u recenici i ispisuje rezultat u obliku: "<rijec>: <broj_ponavljanja>
	c) igra scrabble (vidi u nastavku), koja ispisuje ukupan broj bodova za unesenu rijec.
	d) napravi metodu koja prima vrijednost te od te vrijednosti ispisuje sve brojeve slijedno. program treba na svakom broju koji je djeljiv sa:
		-> 3 ispisati "pling"
		-> 5 ispisati "plang"
		-> 7 ispisati "plong"
		-> ako su djeljivi sa vise od jednog broja, ispisati i jedno i drugo (i trece). npr. ako je unesen broj 105, treba na njegovom mjestu ispisati "plingplangplong" 

SCRABBLE:
Slovo                           Vrijednost
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
'''


class Rijeci:
    def __init__(self) -> None:
        while True:
            self.recenica = input("Unesi recenicu, min. 3 rijeci: ")
            self.__splitaj_recenicu()
            if len(self.splitana_recenica) >= 3:
                break
            print('Neispravan unos!')

    def __splitaj_recenicu(self):
        self.splitana_recenica = list()
        znakovi_za_izbacit = '?!.,\'"'
        spl_rec = self.recenica.split(' ')
        for rijec in spl_rec:
            for znak in znakovi_za_izbacit:
                rijec = rijec.strip(znak)
            self.splitana_recenica.append(rijec.lower())

    def akronim(self):
        sortirane_rijeci = sorted(self.splitana_recenica, key=len, reverse=True)
        for rijec in self.splitana_recenica:
            if rijec in sortirane_rijeci[:3]:
                print(rijec[0].upper(), end='')
        print()

    def prebroji(self):
        dict_rijeci = dict()
        for rijec in self.splitana_recenica:
            if rijec in dict_rijeci.keys():
                dict_rijeci[rijec] += 1
            else:
                dict_rijeci[rijec] = 1
        sortirani_prebroj = dict(sorted(dict_rijeci.items(), key=lambda item: item[1], reverse=True))
        for k, v in sortirani_prebroj.items():
            print(f'{k}: {v}')  

    def scrabble(self):
        vrijednost = 0
        for rijec in self.splitana_recenica:
            for z in rijec:
                if z in 'AEIOULNRST'.lower():
                    vrijednost += 1
                elif z in 'DG'.lower():
                    vrijednost += 2
                elif z in 'BCMP'.lower():
                    vrijednost += 3
                elif z in 'FHVWY'.lower():
                    vrijednost += 4
                elif z == 'K'.lower():
                    vrijednost += 5
                elif z in 'JX'.lower():
                    vrijednost += 8
                else:
                    vrijednost += 10
        print('Vrijednost recenice je', vrijednost)

    def ispisi(self, num: int):
        if num % 3 == 0:
            print('pling', end='')
        if num % 5 == 0:
            print('plang', end='')
        if num % 7 == 0:
            print('plong', end='')
        print()


def main():
    igra = Rijeci()
    igra.akronim()
    igra.prebroji()
    igra.scrabble()
    igra.ispisi(105)

if __name__ == '__main__':
    main()
