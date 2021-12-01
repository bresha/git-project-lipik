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
                self.__uklon()
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
        while True:
            print("Za izlaz upisite '-1'")
            naziv = input("Unesite naziv artikla: ")
            if naziv == '-1':
                break
            if not naziv in self.__inventar.keys():
                print("Nema tog artikla u inventaru")
            else:
                kolicina = self.__unos_kolicine()
                if kolicina == -1:
                    break
                if self.__inventar[naziv] - kolicina >= 0:
                    self.__inventar[naziv] -= kolicina
                else:
                    print("Nema dovoljno artikala")

    def izgradi_kucu(self):
        potrebno_drvo = 5
        potrebno_cigli = 8
        potrabno_crijepa = 4
        jesu_li_komponente_u_invertaru = all(el in self.__inventar.keys() for el in ('drvo', 'cigla', 'crijep'))
        drvo_kolicina = self.__inventar['drvo']
        cigla_kolicina = self.__inventar['cigla']
        crijep_kolicina = self.__inventar['crijep']

        if jesu_li_komponente_u_invertaru and drvo_kolicina >= potrebno_drvo and cigla_kolicina >= potrebno_cigli and crijep_kolicina >= potrabno_crijepa:
            self.__inventar['drvo'] -= potrebno_drvo
            self.__inventar['cigla'] -= potrebno_cigli
            self.__inventar['crijep'] -= potrabno_crijepa
            print("Kuca izgradjena!")
        else:
            print("Kuca nije izgardjena!")
            if drvo_kolicina - potrebno_drvo < 0:
                print(f"Nedostaje {abs(drvo_kolicina - potrebno_drvo)} drva")
            if cigla_kolicina - potrebno_cigli < 0:
                print(f"Nedostaje {abs(cigla_kolicina - potrebno_cigli)} cigli")
            if crijep_kolicina - potrabno_crijepa < 0:
                print(f"Nedostaje {abs(crijep_kolicina - potrabno_crijepa)}")


def main():
    inventar = Inventar()
    inventar.start()
    inventar.izgradi_kucu()

if __name__ == '__main__':
    main()