'''
7. Napiši program koji traži sequence malih slova povezanih s 'underscore'.
'''

import re

text = 'aaaa_bbbb ccc_ddd_kkk'

pattern = re.compile(r'[a-z]+(?:_[a-z]+)+')

print(pattern.findall(text))