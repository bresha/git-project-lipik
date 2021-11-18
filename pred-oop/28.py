'''
28. Neka program omoguci unos do trenutka kad je unesen broj -1. 
Korisnik unosi stringove, a program vraca slucajne recenice iz zbirke mogucih odgovora.
'''
from random import randint

zbirka = [
    "odgovor 1",
    "odgovor 2",
    "odgovor 3",
    "odgovor 4",
    "odgovor 5"
]

while True:
    in1 = input("Unesi string ili '-1' za izlaz: ")
    if in1 == '-1':
        break
    else:
        print(zbirka[randint(0, len(zbirka)-1)])
