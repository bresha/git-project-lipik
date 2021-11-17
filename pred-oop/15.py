'''
15. Napišite program koji ispisuje koliko ima prostih brojeva između 
dva proizvoljna broja (prost broj je broj koji je djeljiv samo sa 1 i sa samim sobom).
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = 1
b = 100

counter = 0
for n in range(a + 1, b):
    if is_prime(n):
        counter += 1

print(counter)