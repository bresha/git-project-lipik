'''
14. Odaberite proizvoljno koordinatu T=(x,y), vrijednosti varijabli x
(stupac) i y (redak) neka budu manje od 10. Program neka ispiše 
polje 10x10 čiji su svi elementi vrijednosti "-" osim koordinate T čija 
je vrijednost "X". 

Primjer: T=(1,1)
- - - - - - - - - -
- X - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
'''

T = (5, 4)

for i in range(1, 11):
    for j in range(1, 11):
        if T[0] == j and T[1] == i:
            print("X", end=' ')
        else:
            print("-", end=' ')
    print()