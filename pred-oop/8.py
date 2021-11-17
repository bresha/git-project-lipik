'''
8. Napišite program koji s tipkovnice učitava proizvoljni cijeli 
troznamenkasti broj. Ako učitani broj nije troznamenkasti, ispišite 
poruku o greški i prekinite daljnje izvođenje programa. U slučaju da 
je učitani broj ispravan, ispišite prvi sljedeći troznamenkasti 
palindrom. Na primjer, ako je učitani broj 120, prvi sljedeći palindrom 
je 121.
'''


in1 = int(input("Unesite troznamenkasti broj: "))

if len(str(in1)) != 3:
    print("greška")
else:
    b = True
    while b:
        in1 += 1
        if len(str(in1)) > 3:
            print("nema troznamenkastog palindroma")
            break
        if str(in1)[0] == str(in1)[2]:
            print(f"palindrom je {in1}")
            break

