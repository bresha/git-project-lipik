'''
3. # Napiši novu funkciju jedinicnaMatrica() koja prima cijeli broj N i vraća jediničnu matricu dimenzija (NxN), ali sadrži samo jednu liniju koda u tijelu funkcije
# Ponovi prošli zadatak koristeći novu funkciju jedinicnaMatrica() i staru lijepaMatrica()
'''

def jedinicna_matrica(n : int):
    return [[1 if j == i else 0 for j in range(n)] for i in range(n)]


def lijepa_matrica(jed_mat : list):
    for lista in jed_mat:
        print(lista)

lijepa_matrica(jedinicna_matrica(5))