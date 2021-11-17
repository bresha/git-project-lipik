'''
3.  Napiši program koji upisuje bodove n plesnih natjecanja. Ispiši zbroj svih bodova tako da odbaciš 
najbolji i najlošiji rezultat.
'''

bodovi = []

while True:
    in1 = input("Unesi bodove ('-1' == 'kraj unosa'): ")
    if in1 == '-1':
        break
    bodovi.append(int(in1))

bodovi.remove(min(bodovi))
bodovi.remove(max(bodovi))

print(sum(bodovi))