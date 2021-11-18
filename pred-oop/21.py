'''
21. Ispišite sljedeće primjere koristeći funkcije i petlju. 
funkcija mora primati varijabilan broj redaka koji ispisuje (npr. pod a), 
unesen broj je 7, jer ima 7 redaka. pod b) je unesen broj 5, jer ima 5 redaka)

a)

*
**
***
****
***
**
*

b)

  *  
 *** 
*****
 *** 
  * 
c)
1010101
 10101 
  101  
   1  
d) 
x x x x
x x x
x x
x
x x
x x x
x x x x
'''


def draw_a(n):
    if n%2 == 0:
        for i in range(1, n//2+1):
            print('*'*i)
    else:
        for i in range(1, (n+1)//2+1):
            print('*'*i)
    for i in range(n//2, 0, -1):
        print('*'*i)


def draw_b(n):
    for i in range(1, n+(n%2), 2):
        print(' '*((n//2+(n%2))-((i+1)//2)) + '*'*i)
    for i in range(n-(n%2)-1, 0, -2):
        print(' '*((n//2+(n%2))-((i+1)//2)) + '*'*i)

def draw_c(n):
    for i in range(n):
        print(' '*i, end='')
        for j in range((n*2-1), i*2, -1):
            if j%2 != 0:
                print(1, end='')
            else:
                print(0, end='')
        print()

def draw_d(n):
    if n%2 == 0:
        for i in range(n//2, 0, -1):
            print('*'*i)
        for i in range(1, n//2+1):
            print('*'*i)
    else:
        for i in range(n//2+1, 0, -1):
            print('*'*i)
        for i in range(1, (n+1)//2):
            print('*'*(i+1))
    

# draw_a(6)
# draw_b(7)
# draw_c(9)
# draw_d(8)