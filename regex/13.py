'''
13. Napiši program koji miče nule iz IP adresa
'''

# Jeli samo leading zeros treba maknuti?

import re

ip = '216.008.094.196'

pattern = re.compile(r'\.[0]+')

new_ip = pattern.sub('.', ip)

print(new_ip)