'''
20. Prebaci format datuma iz našeg u američki.
'''
from datetime import date
import re

date = date.today()

print(date.__str__())

year = re.match(r'\d{4}', date.__str__()).group(0)
month = re.search(r'(?<=-)\d{2}(?=-)', date.__str__()).group(0)
day = re.search(r'(?<=-)\d{2}(?=\Z)', date.__str__()).group(0)

print(f'{day}. {month}. {year}.')