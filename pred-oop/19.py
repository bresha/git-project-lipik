'''
19. Napisi program koji unosi n brojeva i od znamenke desetice svakog broja stvara novi broj.
'''

list_num = []

while True:
    in1 = input("Upisujte brojeve, za prekid upisite 'q': ")
    if in1 == 'q':
        break
    list_num.append(in1)

output = ''
for n in list_num:
    if len(n) >= 2:
        output += n[-2]

print(output)