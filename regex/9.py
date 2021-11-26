'''
9. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojega slijedi bilo što i da završava na 'b'.
'''

import re

text = 'a3993b  anjubabafrit34b'

pattern = re.compile(r'a.*?b')

print(pattern.findall(text))