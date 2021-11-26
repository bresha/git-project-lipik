'''
1. Napiši program koji provjerava sadrži li string određeni set charactera.
    a) a-z 
    b) A-Z 
    c) 0-9
'''

import re

string = 'AZaz09'

print(True if re.search(r'[a-z]+', string) != None else False)
print(True if re.search(r'[A-Z]+', string) != None else False)
print(True if re.search(r'[0-9]+', string) != None else False)
