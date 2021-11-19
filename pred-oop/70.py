'''
70. kreirajte password generator, koji mora sadrzavati sljedece funkcionalnosti:
    a) prilikom generiranja treba prikupiti sljedece podatke od korisnika:
        - koliko lozinki zeli napraviti
        - da li da koristi slova, brojeve, simbole
        - duljinu lozinke
        - kapitalizaciju
    b) nadogradite program tako da korisnik upise rijec (hint). 
    od hint se treba ubaciti u nasumicnom redosljedu i kapitalizaciji u lozinku koja se generira
'''

import random

lower_letters = "abcdefghijklmnopqrstuvwxyz"
symbols = '!#$%&/?'

def get_inputs():
    num_pass = 0
    letters = ''
    nums = ''
    syms = ''
    cap = ''
    length = 0
    create_password_from = []
    hint = ''
    
    while num_pass <= 0:
        num_pass_input = input("Koliko lozinki zelite? Upisite numericki znak: ")
        if num_pass_input.isdigit():
            if int(num_pass_input) > 0:
                num_pass = int(num_pass_input)
                break
        print("Upisali ste neispravan format za broj lozinki.")
    while length <= 0:
        length_input = input("Koliko dugacku lozinku zelite? Unesite numericke znakove: ")
        if length_input.isdigit():
            if int(length_input) >= 8:
                length = int(length_input)
                break
            else:
                print("Duzina lozinke mora biti duza od 7 znakova")
        else:
            print("Niste unijeli numericke znakove.")
    while True:
        while letters == '':
            letters_input = input("Zelite li slova u svojoj lozinci? y/n ")
            if letters_input == 'y' or letters_input == 'n':
                letters = letters_input
                if letters_input == 'y':
                    create_password_from.append('letters')
                break
            else:
                print("Neispravan unos.")
        while nums == '':
            nums_input = input("Zelite li brojeve u svojoj lozinci? y/n ")
            if nums_input == 'y' or nums_input == 'n':
                nums = nums_input
                if nums_input == 'y':
                    create_password_from.append('numbers')
                break
            else:
                print("Neispravan unos.")
        while syms == '':
            syms_input = input("Zelite li simbole u svojoj lozinci? y/n ")
            if syms_input == 'y' or syms_input == 'n':
                syms = syms_input
                if syms_input == 'y':
                    create_password_from.append('symbols')
                break
            else:
                print("Neispravan unos.")
        if len(create_password_from) == 0:
            letters = ''
            nums = ''
            syms = ''
            print("Niste odabrali ni slova ni brojeve ni simbole, od cega cu sastaviti lozinku? ")
        else:
            break
    while cap == '' and letters == 'y':
        cap_input = input("Zelite li kapitalizaciju u svojoj lozinci? y/n ")
        if cap_input == 'y' or cap_input == 'n':
            cap = cap_input
            break
        else:
            print("Neispravan unos.")
    while hint == '':
        hint_input = input("Upisite hint ako ga zelite, ako ga ne zelite upistite '-1': ")
        if hint_input == '-1' or len(hint) <= length:
            hint = hint_input
            break
        else:
            print("Hint je predugacak u odnosu na duzinu lozinke.")


    return num_pass, create_password_from, cap, length, hint

def get_rand_letter():
    idx = random.randint(0, len(lower_letters) - 1)
    return lower_letters[idx]

def get_rand_number():
    return random.randint(0, 9)

def get_rand_symbol():
    idx = random.randint(0, len(symbols) - 1)
    return symbols[idx]

def create_password(create_password_from, cap, length, hint):
    password = ''
    for _ in range(length):
        idx = random.randint(0, len(create_password_from) - 1)
        if create_password_from[idx] == 'letters':
            c = get_rand_letter()
            if cap == 'y':
                c = c.upper()
            password += c
        if create_password_from[idx] == 'numbers':
            n = get_rand_number()
            password += str(n)
        if create_password_from[idx] == 'symbols':
            s = get_rand_symbol()
            password += s
    if hint != '-1':
        hint_split = list(hint)
        pass_split = list(password)
        index_list = list(range(len(pass_split)))
        while len(hint_split) > 0:
            random.shuffle(index_list)
            idx = index_list.pop()
            h = hint_split.pop()
            pass_split[idx] = h
        password = ''.join(pass_split)

    return password

def main():
    num_pass, create_password_from, cap, length, hint = get_inputs()
    for _ in range(num_pass):
        print(create_password(create_password_from, cap, length, hint))

main()