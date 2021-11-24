'''
2. Ponudi korisniku unos dok ne unese '!#quit$', svaku liniju zapisuj u datoteku.
'''

unos = input("Unos: ")
while unos != "!#quit$":
    with open("datoteka2.txt", 'a') as f:
        f.write(unos)
        f.write("\n")
    unos = input("Unos: ")
