'''
1. napravite 2D matricu dimenzija 10, postavite vrijednosti pomocu random(0, 10) i ispisite ju.
'''

import numpy as np

x = np.random.randint(0, 10,(10,10))
print(x)

'''
2. iz matrice iz prethodnog zadatka, ispisite sljedece:
    a) dijagonale matrice
    b) stupce matrice odvojene zarezom
    c) koordinate: [3, 8], [10, 10], [5, 5] - nadogradite tako da korisnik moze unijeti koordinate koje zeli ispisati.
'''

print(x.diagonal())

for i in range(x.shape[1]):
    print(x[:, i], end=',')

print(x[3,8])