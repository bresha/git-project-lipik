'''
5. Nadograditi 4 na način da pri pokretanju programa se korisniku nudi izbor:
    1 - dodavanje knjiga
    2 - izlistavanje knjiga
    3 - izlaz iz programa
'''

from os.path import exists

ime_datoteke = 'knjige2.txt'

def unos_stavke(upit):
    return input(upit)

def unos_knjige():
    naslov = unos_stavke("Unesite naslov knjige: ")
    if naslov == "!#quit$":
        return False
    autor = unos_stavke("Unesite autora knjige: ")
    if autor == "!#quit$":
        return False
    godina_izdanja = unos_stavke("Unesite godinu izdanja knjige: ")
    if godina_izdanja == "!#quit$":
        return False
    cijena = unos_stavke("Unesite cijenu knjige: ")
    if cijena == "!#quit$":
        return False
    with open(ime_datoteke, 'a') as f:
        f.write(f"{naslov},{autor},{godina_izdanja},{cijena}\n")
    return True

def izlistavanje_knjiga():
    if exists(ime_datoteke):
        with open(ime_datoteke, 'r') as f:
            for l in f:
                naslov, autor, godina_izdanja, cijena = tuple(l.split(','))
                print("Naslov:", naslov)
                print("Autor:", autor)
                print("Godina izdanja:", godina_izdanja)
                print("Cijena:", cijena)
    else:
        print("Nema knjiga u bazi.")

def main():
    while True:
        print("Glavni izbornik:")
        print("1 - dodavanje knjiga")
        print("2 - izlistavanje knjiga")
        print("3 - izlaz iz programa")
        unos = input("Unos: ")
        if unos == "3":
            break
        elif unos == '2':
            izlistavanje_knjiga()
        elif unos == "1":
            if not unos_knjige():
                break
        else:
            print("Neispravan izbor!")

main()