'''
4. # napiši funkciju jediničnaMatricaNumpy() koja prima cijeli broj N i vraća jediničnu matricu dimenzija (NxN), te koristi biblioteku NumPy na praktičan način
# neka funkcija sadrži maksimalno do dva reda - istrazi NumPy biblioteku i njene funkcionalnosti.

[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]

[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
'''

import numpy as np

def jedinicna_matrica_numpy(n:int):
    return np.eye(n)

print(jedinicna_matrica_numpy(5))