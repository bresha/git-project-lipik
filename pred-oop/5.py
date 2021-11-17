'''
5. Kreiraj listu koja se sastoji od stringova i brojeva, te odvoji brojeve i stringove u zasebne liste
'''

list_1 = ["a", 1, "b", 2]

list_str = []
list_num = []

for el in list_1:
    if isinstance(el, str):
        list_str.append(el)
    else:
        list_num.append(el)

print(list_str)
print(list_num)