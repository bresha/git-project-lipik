'''
23. Napiši funkciju koja će za neki input broj vratiti nested listu s dužinama sub-lista koje se 
    povećavaju za 1.
	Rezultat bi trebao izgledati ovako: 
		pyramid(0) => [ ]
		pyramid(1) => [ [1] ]
		pyramid(2) => [ [1], [1, 1] ]
		pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
		pyramid(4) => ...
'''

def pyramid(num):
    output = []
    for i in range(num):
        ones = []
        for _ in range(i+1):
            ones.append(1)
        output.append(ones)
    return output

print(pyramid(0))
print(pyramid(1))
print(pyramid(2)) 
print(pyramid(3)) 
print(pyramid(4))