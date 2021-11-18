'''
25. napisite funkciju koja prima string oblika "<predmet>, <cijena>, <kolicina>" (npr. "kruh, 7.5, 5"), 
koji bi simulirao policu neke trgovine. 
program treba razdvojiti navedeni string te zasebne elemente spremiti u rjecnik. 
rjecnik se treba spremiti u listu proizvoda. 
simuliraj kupovinu: kada kupac kupi proizvod (ili broj proizvoda), 
njegova kolicina se treba umanjiti za iznos. 
ukoliko je kolicina 0, predmet se treba ukloniti sa police.
'''

proizvodi = []


def nadji_proizvod(predmet):
    for proizvod in proizvodi:
        if proizvod['predmet'] == predmet:
            return proizvod

while True:
    in1 = input("Odaberite '1' za unos proizvoda, '2' za prodaju, '0' za izlaz: ")
    if in1 == '0':
        break
    elif in1 == '1':
        while True:
            in2 = input("Unesite proizvod u formatu 'predmet, cijena, kolicina' ili unesite '0' za izlaz: ")
            if in2 == '0':
                break
            else:
                spl = in2.split(', ')
                proizvod = {}
                proizvod['predmet'] = spl[0]
                proizvod['cijena'] = float(spl[1])
                proizvod['kolicina'] = int(spl[2])
                proizvodi.append(proizvod)
    elif in1 == '2':
        kosarica = []
        while True:
            in3 = input("Unesite proizvod koji želite prodati u formatu 'predmet, kolicina', za potvrdu kupovine unesite '1', za izlaz unesite '0': ")
            if in3 == '0':
                for vraceni_proizvod in kosarica:
                    proizvod = nadji_proizvod(vraceni_proizvod)
                    if proizvod != None:
                        proizvod['kolicina'] += vraceni_proizvod['kolicina']
                    else:
                        proizvodi.append(vraceni_proizvod)
                break
            elif in3 == '1':
                suma = 0
                for proizvod in kosarica:
                    suma += proizvod['kolicina'] * proizvod['cijena']
                    print(f"{proizvod['predmet']}, {proizvod['kolicina']}, {proizvod['cijena']}")
                print(f"Sveukupno: {suma}")
                kosarica = []
            else:
                predmet, kolicina = tuple(in3.split(', '))
                kolicina = int(kolicina)
                proizvod = nadji_proizvod(predmet)
                if proizvod != None:
                    if proizvod['kolicina'] > kolicina:
                        proizvod['kolicina'] -= kolicina
                        prodani_proizvod = proizvod.copy()
                        prodani_proizvod['kolicina'] = kolicina
                        kosarica.append(prodani_proizvod)
                    elif proizvod['kolicina'] == kolicina:
                        proizvodi.remove(proizvod)
                        kosarica.append(proizvod)
                    else:
                        print(f"Nema dovoljno proizvoda na stanju, (stanje {proizvod['predmet']} = {proizvod['kolicina']}), unijeti ponovno")
                else:
                    print("Nema takvog proizvoda u trgovini.")
