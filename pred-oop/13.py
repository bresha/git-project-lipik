'''
13. Napišite program koji će inicijalizirati varijablu n na proizvoljnu 
cjelobrojnu vrijednost. Vrijednost varijable n neka predstavlja red 
tablice. Ispisati tablicu veličine n redaka i n stupaca. Vrijednost 1 
neka se nalazi na glavnoj dijagonali, a vrijednost 0 na svim ostalim 
mjestima. U nastavku slijedi primjer za n=5:
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1

Napomena: za ispis vrijednost, tako da se nakon ispisa vrijednosti 
dane print() funkciji ne ispiše novi redak koristiti sljedeću 
sintaksu: print(vrijednost, end='')
'''

n = int(input("Unesi cijeli broj: "))
for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()