'''
8. napravite klasu za inventar. implementirajte sljedece funkcionalnost:
	a) korisnicko sucelje sa sljedecim opcijama: unesi predmet u inventar, ukloni predmet iz inventara, izlaz. broj kolicine u inventaru NE SMIJE biti negativan.
	b) za dodavanje: npr ako unesem drvo i 3, ako drvo vec ne postoji u inventaru, treba se napraviti novi kljuci i pridruziti vrijednost 3. 
    ukoliko postoji, vrijednost mu se treba uvecati za 3.
	c) za uklanjanje: npr ako unesem drvo i 3, ako drvo ne postoji u inventaru, nista se nece dogoditi. 
    ukoliko postoji, treba se od njega oduzeti navedeni broj.
	d) napravite i metodu za izgradnju kuce, koja ce od sljedecih materijala izgraditi kucu (ako je moguce) 
    te ih ukloniti iz inventara i ispisati: "kuca izgradjena!": 5x drvo, 8x cigla, 4x crijep. 
    ukoliko izgradnja kuce nije moguca, potrebno je ispisati odgovarajucu poruku 
    (mozete li nadograditi i da ispise sto je jos potrebno od materijala da bi se kuca mogla izgraditi?)
'''

class Inventar:
    def __init__(self) -> None:
        self.__inventar = dict()

    def start(self):
        while True:
            print("Odaberite:")
            print("1) Unos predmeta u inventar")
            print("2) Ukloni predmet iz inventara")
            print("3) Izlaz")
            odabir = input(">> ")
            if odabir == '1':
                self.__unos()
            elif odabir == '2':
                pass
            elif odabir == '3':
                break
            else:
                print("Pogresan odabir!")

    def __unos(self):
        while True:
            print("Za izlaz upisite '-1'")
            naziv = input("Unesi naziv artikla: ")
            if naziv == '-1':
                break
            kolicina = int(self.__unos_kolicine())
            if kolicina == -1:
                break
            if naziv in self.__inventar.keys():
                self.__inventar[naziv] += kolicina
            else:
                self.__inventar[naziv] = kolicina

    def __unos_kolicine(self):
        while True:
            kolicina = input("Unesi kolicinu: ")
            if kolicina.isdigit():
                return kolicina
            else:
                print("Unijeli ste neispravan izraz za kolicinu!")

    def __uklon(self):
        pass
