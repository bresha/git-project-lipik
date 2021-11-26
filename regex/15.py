'''
15. Napiši program koji traži dvoznamenkaste i troznamenkaste brojeve (0-9) u bilo kojem stringu.
'''

import re

text = '091 9875 987 2 89'

pattern = re.compile(r'(?<=\A)\d{2,3}(?=\D|\Z)|(?<=\D)\d{2,3}(?=\D|\Z)')

print(pattern.findall(text))