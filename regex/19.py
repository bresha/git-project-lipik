'''
19. Napiši program koji izbacuje samo brojeve iz nekog URL-a.
'''

import re

url = 'http://web091-0m09home'

pattern = re.compile(r'\D')

numbers = pattern.sub('', url)

print(numbers)