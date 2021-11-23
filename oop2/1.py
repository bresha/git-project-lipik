'''
1. napravite klasu Prva i Druga. neka obje imaju po 2 atributa i po jednu metodu za ispis proizvoljnog teksta. 
izvedite drugu klasu iz prve te ispisite sva 4 atributa koristeci izvedenu klasu.
'''

class Prva:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
class Druga(Prva):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d

    def ispisi(self):
        print(self.a, self.b, self.c, self.d)


druga = Druga(1, 2, 3, 4)
druga.ispisi()