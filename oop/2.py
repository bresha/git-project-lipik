'''
2. napravite klasu za Obrada_stringa. klasa treba imati mogucnosti da iz nekog stringa napravi sljedece (u obliku metoda):
    a) svaku rijec spremi u listu
    b) ispisuje broj velikih i malih slova, brojeva, znakova
    c) pretvorbu cijelih brojeva u rimske ekvivalente
    d) unazadno ispisuje rijec po rijec (npr ako je uneseno "ja sam" treba ispisati "aj mas")
    e) preoblicavanje slova, koja sadrzi sljedece funkcionalnosti: kapitalizacija svakog slova, uppercase cijelog stringa, spajanje stringa u jednu rijec i mijesanje slova
    f) filtriranje brojeva ili slova, ovisno o trazenom
napravite objekte, pozovite i testirajte program.
'''
import random


class Obrada_stringa:
    def __init__(self, string):
        self.string = string
        self.spremi_u_listu()

    def spremi_u_listu(self):
        self.str_lista = self.string.split(' ')
    
    def ispisi_vrste_i_kolicinu_znakova(self):
        velika_slova = 0
        mala_slova = 0
        brojevi = 0
        znakovi = 0
        for c in self.string:
            if c.isupper():
                velika_slova += 1
            if c.islower():
                mala_slova += 1
            if c.isdigit():
                brojevi += 1
            if not c.isalnum():
                znakovi += 1

        print(f"Velikih slova ima {velika_slova}, malih slova ima {mala_slova}, brojeva ima {brojevi}, znakova ima {znakovi}")

    def pretvori_u_rimske(self):
        lista_brojeva = [int(x) for x in self.str_lista if x.isdigit()]
        for num in lista_brojeva:
            print(self.int_to_romans(num), end=' ')
        print()

    def int_to_romans(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def ispisi_unatrag(self):
        for word in self.str_lista:
            print(word[::-1], end=' ')
        print()

    def kapitaliziraj(self):
        for word in self.str_lista:
            print(word.capitalize(), end=' ')
        print()

    def sva_velika(self):
        print(self.string.upper())

    def spoji_string(self):
        print(''.join(self.str_lista))

    def izmjesaj_slova(self):
        lista_znakova = list(self.string)
        random.shuffle(lista_znakova)
        print(''.join(lista_znakova))

    def filtriraj(self, c):
        for word in self.str_lista:
            if c in word:
                print(word)

s = Obrada_stringa("15 je veci od 14")
s.ispisi_vrste_i_kolicinu_znakova()
s.ispisi_unatrag()
s.pretvori_u_rimske()
s.kapitaliziraj()
s.sva_velika()
s.spoji_string()
s.izmjesaj_slova()
s.filtriraj('e')