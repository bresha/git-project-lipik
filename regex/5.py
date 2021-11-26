'''
5. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi 3 'b'
'''

import re

text = 'some  abbbx'

pattern = re.compile(r'ab{3}(?=[^b]|$)')

print(pattern.findall(text))