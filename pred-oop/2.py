'''
2. Napravi obrtaljku od unesenog stringa te na svakom drugom mjestu pridruzi nasumičan broj.
'''

from random import randint

def obrtaljka(str_a):
    r_str = str_a[::-1]
    output = ''
    for c in r_str:
        output += c + str(randint(0, 9))
    return output

str_b = 'hrvoje'

print(obrtaljka(str_b))
