'''
18. Pronađi sve substringove 'exercises' u 'Python exercises, PHP exercises, C# exercises'.
'''


import re

text = 'Python exercises, PHP exercises, C# exercises'

pattern = re.compile(r'exercises')
for m in pattern.finditer(text):
    print(m.span())
