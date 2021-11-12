'''
8 Unesi neki nasumični broj kojeg ćeš uzeti kao vrijednost duljine liste u koju se trebaju spremiti vrijednosti od 0 do 1001. 
	Ispiši sljedeće vrijednosti na ekran:
		a) medijan
		b) mod
		c) aritmetičku vrijednost
		d) sve brojeve koji se u definiranoj listi nalaze ispred vrijednosti koju smo izračunali kao medijan navedene liste
		e) sve brojeve koji su manji od vrijednosti koju smo izračunali kao medijan navedene liste 

	*Bonus: Napravite novu listu koja sadrži samo vrijednosti koje su za 10% veće ili manje od aritmetičke sredine
'''

import random

broj = random.randint(0, 1001)

lista_brojeva = [random.randint(0, 1001) for _ in range(broj)]
lista_brojeva.sort()


def arit_sred(lista):
    return sum(lista) / len(lista)

def medijan(lista):
    idx = len(lista) // 2
    if len(lista) % 2 == 0:
        return arit_sred([lista[idx - 1], lista[idx]])
    else:
        return lista[idx]
    
def mod(lista):
    return max(set(lista), key=lista.count)

def vrijednosti_manje_od_medijana(lista):
    med = medijan(lista)
    lista_vrijed = []
    for el in lista:
        if el < med:
            lista_vrijed.append(el)

    return lista_vrijed


print(f"Medijan {medijan(lista_brojeva)}")
print(f"Mod {mod(lista_brojeva)}")
print(f"Arit sred {arit_sred(lista_brojeva)}")
print(vrijednosti_manje_od_medijana(lista_brojeva))

