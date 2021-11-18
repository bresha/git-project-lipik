'''
26. vas omiljeni carobni aparat za kavu je podivljao. 
aparat treba ispitivati korisnika za kavu sve dok on ne unese "Q" ili 0. 
aparat prihvaca samo kovanice od 2kn ili 5kn. 
kada korisnik ubaci kovanicu od 5kn, aparat nausmicno izbacuje dvije kave. 
kada korisnik ubaci kovanicu od 2kn, aparat nasumicno izbaci jednu kavu. 
ako aparat sakupi 20kn, on se magicno napuni za 3 (nasumicne) kave. 
neka set sljedeceg oblika simbolizira pocetnu kolicinu kave u aparatu: 
dict_kava = {"turska": 4, "latte": 3, "espresso": 7, "makiyato": 5}. 
'''
import random

dict_kava = {"turska": 4, "latte": 3, "espresso": 7, "makiyato": 5}
svakih_20kn = 0

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
        for _ in range(2):
            kava = rand_kava_izbaci()
            svakih_20kn += 5
            print(f"Dobili ste {kava}")
    elif ubaceno == '2' and kolicina_kava() >= 1:
        kava = rand_kava_izbaci()
        svakih_20kn += 2
        print(f"Dobili ste {kava}")
    elif (ubaceno == '5' and kolicina_kava() < 2) or (ubaceno == '2' and kolicina_kava() < 1):
        print("Nema dovoljno kave, vracam novac.")
    else:
        print("Ubacili ste nepoznatu kovanicu!")