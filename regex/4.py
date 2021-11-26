'''
4. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi jedno ili dva 'b'
'''

import re

text = 'some  abbb'

pattern = re.compile(r'ab{1,2}(?=[^b]|$)')

print(pattern.findall(text))