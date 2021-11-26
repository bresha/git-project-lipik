'''
12. Napiši program koji provjerava i vraća rezultat 
ako se u stringu pojavljuju samo velika i mala slova, brojevi i underscore.
'''

import re

text = 'VELIKAmala456_'

pattern = re.compile(r'\w+\Z')

m = pattern.match(text)

print(m.group(0) if m else None)