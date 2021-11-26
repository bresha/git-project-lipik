
'''
8. Napiši program koji traži sequence velikih slova iza kojih se nalaze mala slova.
'''

import re

text = 'abcZH abcZBGnju abcZHJ345 anvZHG'

pattern = re.compile(r'[a-z]+[A-Z]+(?=\w|\s|$)')

print(pattern.findall(text))