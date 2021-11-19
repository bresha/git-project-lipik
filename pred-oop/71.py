'''
71. napravite tipicnog "chat bota" neke drzavne firme. 
bot treba primati input korisnika te ako se odredjena rijec u stringu 
poklapa sa nekim od njemu predefiniranih stringova ili rijeci, ispisati odgovarajucu poruku. 
npr. ako je korisnik unio "pozdrav, ja sam Alen i radim za mirovinsko osiguranje". 
bot treba kao prvi string ispisati: "pozdrav, ja sam bot i napravljen pomocu AI", 
zatim (zbog rijeci mirovinsko), ispisati: " hrvatski zavod za mirovinsko osiguranje je trenutno na pauzi". 
unesite po zelji 20ak razlicitih stringova te simulirajte neki razgovor/temu po zelji.
'''

responses = {
    "pozdrav" : "Pozdrav, ja sam bot i napravljen sam pomocu AI!",
    "bok": "Pozdrav, ja sam bot i napravljen sam pomocu AI!",
    "cao": "Pozdrav, ja sam bot i napravljen sam pomocu AI!",
    "ai": "AI oznacava umjetnu inteligenciju, ja sam umjetan ali sam inteligentan :)",
    "radis": "Ja odgovaram na pitanja o Vladi Republike Hrvatske.",
    "bavis": "Ja odgovaram na pitanja o Vladi Republike Hrvatske.",
    "vlada": "Vlada Republike Hrvatske je sastavljena od premijera i više ministara, sve sami prekrasni ljudi!",
    "vladi": "Vlada Republike Hrvatske je sastavljena od premijera i više ministara, sve sami prekrasni ljudi!",
    "ministar": "Vlada Republike Hrvatske ima razna ministarstva koje vode ministri ali ne bi sad u detalje.",
    "ministri": "Vlada Republike Hrvatske ima razna ministarstva koje vode ministri ali ne bi sad u detalje.",
    "premijer": "Premier nam je Andrej Plenković.",
    "plenki": "Ne smijemo ga tako oslovljavati.",
    "ministarstava": "Ima puno ministarstava, tko bi sad isao u detalje, ni ja ne znam cemu sva služe.",
    "ministarstavo": "Ima puno ministarstava, tko bi sad isao u detalje, ni ja ne znam cemu sva služe.",
    "bira": "Vladu biraju građani Republike Hrvatske.",
    "gdje": "Premijer i ministri su na pauzi.",
    "else": "Ne prepoznajem taj upit, ipak nisam tako inteligentan :(",
}

def get_responses(in1):
    cur_res = []
    in1_split = in1.split(' ')
    for i in range(len(in1_split)):
        in1_split[i] = in1_split[i].replace('.', '').replace(',', '').replace('!', '').replace('?', '').lower()
    for w in in1_split:
        if w in responses.keys():
            cur_res.append(responses[w])
    if len(cur_res) == 0:
        cur_res.append(responses['else'])
    return cur_res

while True:
    in1 = input(">> ")
    cur_res = get_responses(in1)
    for res in cur_res:
        print(res)
