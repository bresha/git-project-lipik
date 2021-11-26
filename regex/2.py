'''
2. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi nula ili više 'b'
'''

import re

text = 'some  atext'

print(True if re.search(r'ab*', text) != None else False)