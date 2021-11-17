'''
4. Kreiraj listu brojeva i pretvori svaki element u listi u njegov kvadrat
'''

list_1 = [1, 2, 3, 4, 5]

for i in range(len(list_1)):
    list_1[i] = list_1[i]**2

print(list_1)