'''
25. Potrebno je napraviti algoritam koji prima string liste s tri objekta. Navedeni objekti su zapravo rječnici(dictionaries) s 2 key-value para - gdje su “name” i “price” ključevi. 
Nazovite navedeni string json_string

	Primjer: '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'

	Navedeni algoritam mora riješiti sljedeće zadatke: 
		-->sortirati elemente liste po “price” ključu tako da ide od najmanje do najveće vrijednosti koja se nalazi pod “price”
		-->ukoliko su cijene dvaju proizvoda iste, onda mora sortirati ta dva proizvoda po abecedi unazad.
		-->Mora biti reproducibilan, tj. taj algoritam morate importati u drugoj skripti pod nazivom main.py 

	Testiranje: 
		'[{"name":"pivo","price":7.99},{"name":"vino","price":35.99},{"name":"rakija","price":50}]'
		'[{"name":"paprika","price":11.99},{"name":"jaja","price":11.99},{"name":"kobasice","price":18.04}]'
		'[{"name":"sir","price":35.14},{"name":"slanina","price":40.54},{"name":"rajčica","price":9.99}]'
'''

import json

json_string = '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'

def sort_by_price(json_string):
    items = json.loads(json_string)
    sorted_by_alfabet = sorted(items, key=lambda item: item['name'])
    sorted_by_price = sorted(sorted_by_alfabet, key=lambda item: item['price'])
    return sorted_by_price


print(sort_by_price(json_string))
print(sort_by_price('[{"name":"pivo","price":7.99},{"name":"vino","price":35.99},{"name":"rakija","price":50}]'))
print(sort_by_price('[{"name":"paprika","price":11.99},{"name":"jaja","price":11.99},{"name":"kobasice","price":18.04}]'))
print(sort_by_price('[{"name":"sir","price":35.14},{"name":"slanina","price":40.54},{"name":"rajčica","price":9.99}]'))