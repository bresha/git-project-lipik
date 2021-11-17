'''
9. Napišite program koji učitava cijele brojeve sve dok je unesena 
vrijednost veća od 0. Pronađite koji od učitanih brojeva ima najmanju 
sumu znamenki te ispišite taj broj i sumu.
'''
list_num = []
while True:
    in1 = int(input("Unesi cijeli broj: "))
    if in1 <= 0:
        break
    list_num.append(in1)

least_sum_index = -1
least_sum = 0
for i, n in enumerate(list_num):
    current_sum = sum(list(map(int, list(str(n)))))
    if least_sum == 0:
        least_sum_index = 0
        least_sum = current_sum
    if current_sum < least_sum:
        least_sum = current_sum
        least_sum_index = i

print(list_num[least_sum_index], least_sum)
