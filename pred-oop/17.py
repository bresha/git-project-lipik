'''
17. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz 
znakova. Ispišite koliko velikih slova se nalazi u nizu. Ako je neko od 
unesenih slova u nizu "A", brojanje velikih slova je potrebno prekinuti 
i ispisati informaciju da je veliko slovo "A" pronađeno.
'''

s = "skIdeVpckiJnAcrt"
counter = 0
flag = True

for c in s:
    if c.isupper():
        if c == 'A':
            print("Veliko A je pronađeno")
            flag = False
            break
        counter += 1

if flag:
    print(f"Velikih slova u nizu je {counter}")
