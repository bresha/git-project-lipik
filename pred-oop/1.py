'''
1. Napiši program koji učitava listu i briše sve duplikate iz te liste te ispisuje novu listu s 
obrisanim duplikatima.
'''

def remove_duplicates(list_a):
    return list(set(list_a))

list_b = [1, 2, 3, 1, 3, 4, 5]

print(remove_duplicates(list_b))