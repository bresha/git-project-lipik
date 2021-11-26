'''
6. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi 2 do 3 'b'
'''


import re

text = 'some  abbbbx'

pattern = re.compile(r'ab{2,3}(?=[^b]|$)')

print(pattern.findall(text))