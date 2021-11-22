'''
9. napravite klasu za usitnjavanje ili razmjenu novca. 
unutar klase osmislite sustav koji bi sadrzavao listu cijelih brojeva (novcanice unutar kase). 
metoda unutar klase bi primala neki broj. 
program treba vratiti sumu elemenata liste, koji bi tvorili uneseni broj, odnosno da li je uopce moguce izvratiti tocan iznos, s obzirom na novac u kasi (listi). 
npr ako je lista [10, 20, 50, 100, 200], a korisnik unese 180kn, program treba izbaciti iz liste 10, 20, 50, 100 te vratiti da je to moguce napraviti.
'''

class Kasa:
    izvraceno = []
    def __init__(self):
        self.kasa = [10, 20, 50, 100, 200]

    def izvrati(self, iznos):
        for n in self.kasa[::-1]:
            if iznos - n >= 0:
                iznos -= n
                self.izvraceno.append(n)
        if iznos == 0:
            return self.izvraceno
        else:
            return None

k = Kasa()
print(k.izvrati(180))