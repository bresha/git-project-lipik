'''
4. kreirajte klasu Vozilo, koja sadrzi sljedece atribute: marka, model, masa, kilometraza, max brzina, boja, cijena. 
napravite 2 objekta sa razlicitim atributima. 
nakon postavljanja, izmijenite boju u crvenu, kilometrazu postavite na 10000, max brzinu spustite za 15 i cijenu spustite za 10%. 
usporedite aute te ispisite koji od njih ima vecu max brzinu, kilometrazu i manju cijenu. 
'''

class Vozilo:
    def __init__(self, marka, model, masa, kilometraza, max_brzina, boja, cijena):
        self.marka = marka
        self.model = model
        self.masa = masa
        self.kilometraza = kilometraza
        self.max_brzina = max_brzina
        self.boja = boja
        self.cijena = cijena


audi = Vozilo('audi', 'q7', 2000, 200000, 250, 'siva', 50000)
bmw = Vozilo('bmw', 'q530', 1500, 250000, 250, 'plava', 6000)
audi.boja = 'crvena'
audi.kilometraza = 10000
audi.max_brzina -= 15
audi.cijena -= audi.cijena * 0.1

if audi.max_brzina > bmw.max_brzina:
    print("Audi ima vecu brzinu.")
elif audi.max_brzina < bmw.max_brzina:
    print("Bmw ima vecu brzinu.")
else:
    print("Auti imaju jednaku brzinu")

if audi.kilometraza > bmw.kilometraza:
    print("Audi ima vecu kilometrazu.")
elif audi.kilometraza < bmw.kilometraza:
    print("Bmw ima vecu kilometrazu.")
else:
    print("Auti imaju jednaku kilometrazu")

if audi.cijena < bmw.cijena:
    print("Audi ima manju cijenu.")
elif audi.cijena > bmw.cijena:
    print("Bmw ima manju cijenu.")
else:
    print("Auti imaju jednaku cijenu")