'''
1. # napiši funkciju koja za uneseni broj N ispisuje šahovnicu dimenzija (NxN)
# crno polje: ■, bijelo polje: □ 
(5x5)
■  □  ■  □  ■  
□  ■  □  ■  □  
■  □  ■  □  ■  
□  ■  □  ■  □  
■  □  ■  □  ■ 
'''

def draw_chessboard(n):
    for i in range(n):
        if i % 2 != 0:
            for j in range(n):
                if j % 2 == 0:
                    print('□', end=' ')
                else:
                    print('■', end=' ')
        else:
            for j in range(n):
                if j % 2 != 0:
                    print('□', end=' ')
                else:
                    print('■', end=' ')
        print()

draw_chessboard(3)