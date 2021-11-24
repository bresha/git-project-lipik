'''
4. Omogući unos, dok se ne unese '!#quit$'. Pitajte korisnika želi li unjeti knjigu.
Omogući popisivanje knjiga u skladištu.
Svaka knjiga ima naslov, autora, godinu izdanja, te cijenu. Nakon unosa svake knjige, upitajte korisnika
želi li unjeti još jednu knjigu. Svaku knjigu zapisati u datoteku.
'''

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
    with open("knjige.txt", 'a') as f:
        f.write(f"{naslov},{autor},{godina_izdanja},{cijena}\n")
    return True

def main():
    while True:
        unos = input("Želite li unijeti knjigu (da/ne): ")
        if unos == "ne":
            break
        elif unos == "da":
            if not unos_knjige():
                break
        else:
            print("Neispravan izbor!")

main()