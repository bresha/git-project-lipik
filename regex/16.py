'''
16. Napiši program koji traži određene riječi u stringu:
    Sample text : 'The quick brown fox jumps over the lazy dog.' Searched words : 'fox', 'dog', 'horse'
'''
import re

text = 'The quick brown fox jumps over the lazy dog.'

search_words = ['fox', 'dog', 'horse']

for word in search_words:
    pattern = re.compile(r'\b{}\b'.format(word))
    m = pattern.search(text)
    if m:
        print('found', m.group(0))
