'''
5. 
# 1)
# a) napiši program koji ispisuje sljedeći output:

# ■     ■  
#    ■     
# ■     ■ 

# nazovimo to uzorak "petica"

# b) napiši program koji ispisuje (kvadratice u uzorku petice) u uzorku petice

# ■     ■           ■     ■  
#    ■                 ■     
# ■     ■           ■     ■  
#          ■     ■           
#             ■              
#          ■     ■           
# ■     ■           ■     ■  
#    ■                 ■     
# ■     ■           ■     ■  

# c) napiši funkciju koja generalizira koncept koji smo napravili u zadacima a) i b)
# za unos 1 funkcija treba vratiti kvadratice u uzorku petice, za unos 2 treba vratiti (kvadratice u uzorku petice) u uzorku petice
# za unos 3 treba vratiti (kvadratice u uzorku petice u uzorku petice) u uzorku petice
# itd.
# dobiveni oblik biti ce fraktal, a funkcija koja ga uspjesno obavlja trebala bi biti rekurzivna
'''

def petica():
    for i in range(3):
        for j in range(3):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                print('■', end='  ')
            else:
                print(' ', end='  ')
        print()

# Kako ovo rijesiti?