'''
27. nadogradite prethodni zadatak na nacin da ubacite u aparat i opciju za dodavanje 
mlijeka, secera ili meda u kavu. 
kada korisnik ubaci kovanicu, 
aparat ga treba pitati zeli li kavu sa dodatkom ili ne. 
postavite vrijednost svakog dodatka na 5, koristeci fromkeys. 
ukoliko korisnik zatrazi kavu sa sladilom kojega vise nema u aparatu, 
treba ispisati odgovarajucu poruku te ponuditi korisniku opciju bez dodatka ili povrat novca, 
nakon cega zavrsava sa izvodjenjem. u svim slucajevima treba se ispisati kakva je kava isporucena, 
sa kojim sladilom, koliko novca je ubaceno te koliki je iznos novca u aparatu nakon isporuke kave.
'''

import random

dict_kava = {"turska": 4, "latte": 3, "espresso": 7, "makiyato": 5}
dodatci = dict.fromkeys(["mlijeko", "secer", "med"], 5)
svakih_20kn = 0
stanje = 0

def kolicina_kava():
    return sum(dict_kava.values())

def rand_kava_izbaci():
    moguce_kave = [x for x in dict_kava.keys() if dict_kava[x] > 0]
    idx = random.randint(0, len(moguce_kave) - 1)
    random_kava = moguce_kave[idx]
    dict_kava[random_kava] -= 1
    return random_kava

def rand_kava_ubaci():
    moguce_kave = list(dict_kava.keys())
    idx = random.randint(0, len(moguce_kave) - 1)
    random_kava = moguce_kave[idx]
    dict_kava[random_kava] += 1
    return random_kava

def izbor_dodataka(broj_kava):
    in2 = input("Unesite 'da' ako želite dodatak: ")
    if in2 == "da":
        while True:
            in3 = input("Unesite 'mlijeko', 'secer' ili 'med': ")
            if in3 == 'mlijeko' or in3 == 'secer' or in3 == 'med':
                if dodatci[in3] >= broj_kava:
                    dodatci[in3] -= broj_kava
                    return in3
                else:
                    in4 = input(f"Nema {in3}. Unesite 'da' ako želite kavu bez dodatka: ")
                    if in4 == 'da':
                        return 'bez dodataka'
                    return 'vrati pare'
    else:
        return 'bez dodatka'


while True:
    if svakih_20kn > 20:
        for _ in range(3):
            rand_kava_ubaci()
        svakih_20kn = svakih_20kn - 20
    in1 = input("Ubaci kovanicu od 2 ili 5 kuna! Za izlaz upiši 'Q' ili '0': ")
    ubaceno = in1[0]
    if ubaceno == 'Q' or ubaceno == '0':
        break
    elif ubaceno == '5' and kolicina_kava() >= 2:
        dodatak = izbor_dodataka(2)
        if dodatak == 'vrati pare':
            print(f"Vracam {ubaceno}kn")
            break
        elif dodatak == 'bez dodatka':
            svakih_20kn += 5
            stanje += 5
            for _ in range(2):
                kava = rand_kava_izbaci()
                print(f"Dobili ste {kava}. Ubaceno je {ubaceno}kn, u aparatu je {stanje}kn")
        else: 
            svakih_20kn += 5
            stanje += 5
            for _ in range(2):
                kava = rand_kava_izbaci()
                print(f"Dobili ste {kava} s {dodatak}. Ubaceno je {ubaceno}kn, u aparatu je {stanje}kn")
    elif ubaceno == '2' and kolicina_kava() >= 1:
        dodatak = izbor_dodataka(1)
        if dodatak == 'vrati pare':
            print(f"Vracam {ubaceno}kn")
            break
        elif dodatak == 'bez dodatka':
            kava = rand_kava_izbaci()
            svakih_20kn += 2
            stanje += 2
            print(f"Dobili ste {kava}. Ubaceno je {ubaceno}kn, u aparatu je {stanje}kn")
        else:
            kava = rand_kava_izbaci()
            svakih_20kn += 2
            stanje += 2
            print(f"Dobili ste {kava} s {dodatak}. Ubaceno je {ubaceno}kn, u aparatu je {stanje}kn")
    elif (ubaceno == '5' and kolicina_kava() < 2) or (ubaceno == '2' and kolicina_kava() < 1):
        print("Nema dovoljno kave, vracam novac.")
    else:
        print("Ubacili ste nepoznatu kovanicu!")