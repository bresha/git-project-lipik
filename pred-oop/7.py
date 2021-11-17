'''
7. Učitajte s tipkovnice 2 niza znakova, svaki od tih nizova znakova 
spremite u zasebnu varijablu. Ispišite indekse na kojima se pojavljuju 
ista slova neovisno o veličini ('a' i 'A' tretirati jednako).
'''


a = input("Unesi prvi niz znakova: ")
b = input("Unesi drugi niz znakova: ")

if len(a) > len(b):
    for i in range(len(b)):
        if a[i].lower() == b[i].lower():
            print(i)
else:
    for i in range(len(a)):
        if a[i].lower() == b[i].lower():
            print(i)