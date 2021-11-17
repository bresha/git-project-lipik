'''
12. Napišite program koji s tipkovnice učitava proizvoljni niz znakova. 
Nad učitanim nizom znakova napravite analizu je li taj niz palindrom 
ili nije. Niz je palindrom ako se isto čita slijeva nadesno ili pak 
zdesna nalijevo.
'''

in1 = input("unesi niz znakova: ")

if in1 == in1[::-1]:
    print("niz zankova je palindrom")
else:
    print("niz znakova nije palindrom")