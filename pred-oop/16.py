'''
16. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni 
niz znakova i brojčanu varijablu n. Provjerite je li vrijednost varijable 
n manja od broja znakova u nizu. Ako je vrijednost varijable n veća 
ispišite informaciju o grešci. Ispišite iz niza znakova svako n-to 
slovo. Na primjer, ulazni niz je "ABCDEFGH", n je 2, tada je izlaz 
"ACEG".
'''

s = 'ABCDEFGH'
n = 2

if n >= (len(s) + 1):
    print("error")
else:
    for i in range(0, len(s), n):
        print(s[i], end='')