'''
11. Napiši program koji vraća sve riječi koje sadrže 'z'
'''

import re

text = 'somez tezxt zwith z'

pattern = re.compile(r'[A-Za-z\'\"]*z[A-Za-z\'\"]*')

print(pattern.findall(text))