'''
22. Napišite program za koji traži najveći zajednički djelitelj dvaju brojeva
'''

def greatest_common_div(a, b):
    if a > b:
        b, a = a, b

    div_b = [x for x in range(1, b+1) if b % x == 0]
    div_a = [y for y in range(1, a+1) if a % y == 0]
    for y in div_a[::-1]:
        if y in div_b:
            return y


print(greatest_common_div(18, 48))