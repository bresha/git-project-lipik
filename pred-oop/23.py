'''
23. koristenjem funkcija i naucenog, 
napisi program koji racuna iznos racuna u ovisnosti o transakcijama. 
dnevnik transakcija prikazi ovako (D: 100, W: 200), 
dok ukupan iznos na racunu prikazuje sa (T: 1000). 
ako korisnik unese T = 1000 te povuce iznos od 350 (W: 350), 
aplikacija treba ispisati azurirano stanje T: 650. 
ako nakon toga korisnik uplati iznos na racun, npr. 200 (D: 200), 
program treba uvecati iznos racuna i azurirati ga (T: 850). 
unosom stringa "quit", program prekida se izvodjenje programa.
'''

def sum_transactions(transactions):
    output = 0
    for t in transactions:
        if t[0] == 'T':
            output = t[1]
        elif t[0] == 'W':
            output -= t[1]
        elif t[0] == 'D':
            output += t[1]
        else:
            print("Something went wrong!")
    return output

transactions = []

while True:
    in1 = input("Unesite transakciju ('T: xxx' za pocetno stanje, 'W: xxx' za povlacenje novca, 'D: xxx' za polaganje novca a upisite 'quit' za izlaz: ")
    if in1 == 'quit':
        break
    else:
        flag, amount = tuple(in1.split(': '))
        transaction = (flag, int(amount))
        if flag == 'T':
            transactions.clear()
            transactions.append(transaction)
        elif (flag == 'W' or flag == 'D') and transactions[0][0] == 'T':
            transactions.append(transaction)
            print(f"T: {sum_transactions(transactions)}")
        else:
            print("Wrong input!")
