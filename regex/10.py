'''
10. Napiši program koji vraća zadnju riječ u stringu, zajedno s opcionalnim punktuacijama
'''

import re

text = 'some "text".'

pattern = re.compile(r'[A-Za-z\'\"]+(?:\.|\?|\!)*\Z')

m = pattern.search(text)

print(m.group(0))