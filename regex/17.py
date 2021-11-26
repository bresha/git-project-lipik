'''
17. Za svaku riječ iz zadatka 16. izbaci i od kojeg do kojeg indeksa se pojavljuju
'''

import re

text = 'The quick brown fox jumps over the lazy dog.'

search_words = ['fox', 'dog', 'horse']

for word in search_words:
    pattern = re.compile(r'\b{}\b'.format(word))
    m = pattern.search(text)
    if m:
        print('found', m.group(0), m.span())