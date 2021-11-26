'''
14. Napiši program koji traži postoji li broj na kraju stringa
'''

import re

text = 'text s brojem 0'

pattern = re.compile(r'\d\Z')

m = pattern.search(text)

print(True if m else False)