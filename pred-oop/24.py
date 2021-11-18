'''
24. zadan je rjecnik:
automobil = {
    'kilometri' : 230000,
    'oprema' : ['zimske gume', 'zracni jastuk', 'protuprovalni bacac plamena'],
}
    a) kilometre preuredite tako da dodatno broji i kilometre do servisa. postavite vrijednost na 300.
    b) iz opreme, promijenite "zimske gume" u "ljetne gume" te "zracni jastuk" u "zracni balon"
    c) dodajte polje za unos specifikacije koja sadrzi godinu proizvodnje (1976.), potrosnju (15 litara) 
            i max. brzinu (178 km/h)
    d) dodajte cijenu i postavite je na 45000
    e) dodajte osiguranje (npr. croatia) te postavite vrijednost na True
    f) kada se pozove funkcija 'servis', 
            znaci da se automobil servisirao i promijenile su se sljedece vrijednosti:
        - kilometri do servisa su se postavili na 2000
        - zracni balon postao je 'novi zracni jastuk'
        - ljetne gume promijenjene su na 'cjelogodisnje gume'
        - cijenu uvecajte za 2000
'''

automobil = {
    'kilometri' : 230000,
    'oprema' : ['zimske gume', 'zracni jastuk', 'protuprovalni bacac plamena'],
}

automobil['kilometri'] = {'kilometri': automobil['kilometri'], 'kilometri do servisa': 300}
automobil['oprema'][0] = 'ljetne gume'
automobil['oprema'][1] = 'zracni balon'
automobil['specifikacije'] = {'godina proizvodnje': 1976, 'potrošnja': '15 litara', 'max brzina': '178 km/h'}
automobil['cijena'] = 45000
automobil['osiguranje'] = {'croatia': True}

def servis():
    automobil['kilometri']['kilometri do servisa'] = 2000
    automobil['oprema'][1] = 'novi zracni jastuk'
    automobil['oprema'][0] = 'cjelogodisnje gume'
    automobil['cijena'] += 2000

servis()
print(automobil)