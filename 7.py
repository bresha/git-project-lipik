'''
7. Ispiši vrijednost broja Pi na 4 decimalna mjesta, kvadriraj taj broj te ga podijeli s racionalnim brojem odabranim od strane korisnika (input funkcija) i ispiši rezultat.
'''


import math

pi = round(math.pi, 4)
print(f"Pi na 4 mjesta je {pi}")

pi_sq = pi ** 2

i = float(input("Unesi racionalni broj: "))

print(f"Konačan rezultat je {pi_sq / i}")
