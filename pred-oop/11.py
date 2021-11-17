'''
11. Napišite program koji s tipkovnice učitava cijeli broj n iz intervala [3, 
20]. U slučaju da je unesena vrijednost neispravna, ispisati prikladnu 
poruku na ekran te zatražiti ponovni unos cijelog broja. Nakon 
učitane vrijednosti n, učitajte n parova cijelih brojeva. Nakon što je n
parova brojeva učitano, ispišite parove brojeva koji imaju najveću 
sumu.
'''
pairs = []

def load_pairs():
    in1 = input("Unesite par brojeva odvojen razmakom: ")
    return list(map(int, in1.split(' ')))

while True:
    n = int(input("Unesite cijeli broj od 3 do 20: "))
    if n >= 3 and n <= 20:
        for _ in range(n):
            pair = load_pairs()
            pairs.append(pair)
        break
    else:
        print("Neispravan unos!")

max_sum = 0
max_sum_idx = -1

for i, pair in enumerate(pairs):
    pair_sum = sum(pair)
    if pair_sum > max_sum:
        max_sum = pair_sum
        max_sum_idx = i

print(pairs[max_sum_idx])
