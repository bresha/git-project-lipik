'''
4. Napišite program koji će u varijable a i b spremiti dva dvoznamenkasta broja. U varijablu a pohranite zadnju znamenku broja koji se nalazi u varijabli b, 
a u varijablu b pohranite zadnju znamenku broja koja se nalazi u varijabli a. Ispišite sadržaj varijabli a i b.
'''


a = 20
b = 34

a, b = int(str(b)[-1]), int(str(a)[-1])

print(a, b)