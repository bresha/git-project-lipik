'''
2. # napiši funkciju jedinicnaMatrica() koja prima cijeli broj N i vraća jediničnu matricu dimenzija (NxN)
# napiši funkciju lijepaMatrica() kojoj će se proslijediti jedinična matrica u plošnom obliku te ispisati na vizualno uobičajen način
# zatim, napiši program koji upotrebljava obje funkcije u sinergiji kako bi prikazao tri različite jedinične matrice


#  3  ----input---->  jedinicnaMatrica()  ----output---->  [[1, 0, 0], [0, 1, 0], [0, 0, 1]] ----input---->  lijepaMatrica() ---output---> [1,0,0]

(3x3): 
[1, 0, 0]
[0, 1, 0]
[0, 0, 1]

(4x4): 
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]

(5x5): 
[1, 0, 0, 0, 0]
[0, 1, 0, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 0, 1, 0]
[0, 0, 0, 0, 1]
'''

def jedinicna_matrica(n):
    output = []
    for i in range(n):
        lista = []
        for j in range(n):
            if i == j:
                lista.append(1)
            else:
                lista.append(0)
        output.append(lista)
    return output

def lijepa_matrica(jed_mat : list):
    for lista in jed_mat:
        print(lista)

lijepa_matrica(jedinicna_matrica(5))
