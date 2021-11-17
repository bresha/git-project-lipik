'''
20. Napisi program koji unosi n brojeva i sastavlja novi broj od najvece znamenke u svakom od
brojeva
'''

list_num = []

while True:
    in1 = input("Upisujte brojeve, za prekid upisite 'q': ")
    if in1 == 'q':
        break
    list_num.append(in1)


output = ''

for n in list_num:
    m = 0
    for e in n:
        if int(e) > m:
            m = int(e)
    output += str(m)

print(output)    