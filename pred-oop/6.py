'''
6. S tipkovnice učitavajte cijele brojeve. Prvi upisani broj može biti bilo 
koji cijeli broj. Učitavanje ponavljati dok god je upisani broj strogo 
veći od prethodno upisanog broja. Ispisati sumu svih učitanih brojeva 
osim broja zbog kojeg je prekinuto učitavanje.
'''

list_num = []

while True:
    in1 = int(input("Unesi broj: "))
    if len(list_num) == 0:
        list_num.append(in1)
    else:
        if list_num[-1] < in1:
            list_num.append(in1)
        else:
            break


print(sum(list_num))