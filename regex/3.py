'''
3. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi jedno ili više 'b'
'''

import re

text = 'some  abtext'

print(True if re.search(r'ab+', text) != None else False)