'''
7. napravite program koji izracunava razliku dva unesena niza DNK (jednakih duljina). npr. ako su uneseni: 
"GAGCCTACTAACGGGAT" i 
"CATCGTAATGACGGCCT"
 x x x  x x    xx
program treba ispisati da je razlika 7. mozete li ispisati i parove koji nisu u redu?
'''

def usporedi_DNK(dnk1, dnk2):
    if len(dnk1) == len(dnk2):
        skup = zip(dnk1, dnk2)
        suma = 0
        parovi = list()
        for el in skup:
            if el[0] != el[1]:
                suma += 1
                parovi.append(el)
        print(suma)
        print(parovi)
    else:
        print('Parovi nisu jednakih duzina!')


usporedi_DNK("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")