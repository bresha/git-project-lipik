'''
6. Unesi jedan nasumični broj. 
Ispiši aritmetičku sredinu onoliko brojeva(0-101) koliko je iznosio uneseni nasumični broj.
Navedeni broj uzmi kao vrijednost opsega kruga te ispiši vrijednost polumjera navedenog kruga.
'''

import random
import math

broj = random.randint(0, 101)

lista_brojeva = [random.randint(0, 101) for _ in range(broj)]

if len(lista_brojeva) == 0:
    arit_sred = 0
else:
    arit_sred = sum(lista_brojeva) / len(lista_brojeva)

print(f"Aritmetička sredina je {arit_sred}")

''' O  = 2r pi'''
''' r = O/ 2 pi'''

r = arit_sred / (2 * math.pi)

print(f"Polumjer je {r}")