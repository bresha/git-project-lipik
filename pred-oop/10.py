'''
10. S tipkovnice učitajte proizvoljni niz znakova. Kreirajte novi niz 
znakova koji će sadržavati naizmjence velika i mala slova iz ulaznog 
niza, redom kako se pojavljuju u ulaznom nizu: prvo veliko slovo u 
ulaznom nizu, prvo sljedeće malo slovo u nastavku ulaznog niza, 
prvo sljedeće veliko slovo u nastavku ulaznog niza itd. Novokreirani 
niz ispišite na zaslon. U nastavku se nalazi primjer:

Ulazni niz: ifeFemFEkej83FkW
Izlazni niz: FeFkFkW
'''


in1 = input("Unesi niz nakova: ")

upper = True
for c in in1:
    if c.isupper() == upper and upper == True:
        print(c, end='')
        upper = False
    if c.isupper() == upper and upper == False:
        print(c, end='')
        upper = True
    