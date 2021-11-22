'''
24. Automat s čokoladicama prima bilo koji iznos u kunama i vraća kovanice u sljedećim oblicima:
	1 lipa
	2 lipe
	5 lipa
	10 lipa
	20 lipa
	50 lipa
	1 kuna
	2 kune
	5 kuna
Potrebno je napisati funkciju koju će koristiti navedeni automat s čokoladicama kako bi vratio ostatak novca korisniku. 
Pretpostavka je da automat uvijek vraća najmanji mogući broj kovanica.
Funkcija prima 2 parametra - količinu novca kojeg je korisnik ubacio i cijenu proizvoda
Funkcija vraća listu brojeva. Svaki od tih brojeva predstavlja količinu jedne vrste kovanice.

Primjer: getChange(20, 3.99) -> [1, 0, 0, 0, 0, 0, 1, 0, 3]  ((1lp, 2lp, 5lp, 10lp, 20lp, 50lp, 1kn, 2kn, 5kn))

Testiranje:
get_change(3.14, 1.99) -> [0, 0, 1, 1, 0, 0, 1, 0, 0] 
get_change(4, 3.14) -> [1, 0, 0, 0, 0, 0, 1, 0, 3] 
get_change(0.45, 0.34) -> [1, 0, 0, 0, 0, 0, 1, 0, 3] 
'''

def get_change(amount, price):
    output = []
    amount100 = amount * 100
    price100  = price * 100
    diff = amount100 - price100
    list_of_returns = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    for ret in list_of_returns:
        if diff // ret > 0:
            output.append(int(diff // ret))
            diff = diff - (diff // ret) * ret
        else:
            output.append(0) 
    output.reverse()
    return output

print(get_change(20, 3.99))
print(get_change(3.14, 1.99))