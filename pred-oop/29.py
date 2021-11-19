'''
29. napravite program koji ce simulirati izvlacenje karti iz spila. program mora imati sljedece:
    - spil od 20 karti
    - 4 razlicite boje
    - 5 brojeva za svaku boju
    program treba imati mogucnost povlacenja 3 karte, povlacenja 1 karte, mijesanja spila, 
    zbrajanja bodova (brojevi na kartama).
    kreirajte izbornik sa mogucnoscu izbora opcije (zapocni igru, zavrsi igru) -> 
    ako korisnik odabere "zapocni igru", spil se mijesa te se povlace 3 karte. 
    igraca se zatim pita hoce li povuci dodatnu kartu ili ne. 
    ako odabere novu kartu, ona se dodaje u ruku; u suprotnom se broj bodova usporedjuje sa protivnikom. 
    koristeci random varijablu (12-20), kreirajte protivnika, 
    gdje random varijabla predstavlja njegov broj bodova. 
    program treba racunati trenutni broj bodova te ako on prelazi 20, 
    ispisati "izgubio si" i pitati korisnika zeli li ponovno igrati ili ne. 
    ukoliko igrac pobijedi, treba ispisati poruku: pobijedio si i postaviti pitanje za novom igrom.
'''

import random

def create_deck():
    colors = ['H', 'D', 'S', 'C']
    numbers = list(range(2, 7))
    deck = []
    for c in colors:
        for n in numbers:
            deck.append((n, c))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def pull_card(deck):
    card = deck.pop(0)
    return card

def pull_3_cards(deck):
    cards = []
    for _ in range(3):
        card = pull_card(deck)
        cards.append(card)
    return cards

def hand_to_str(hand):
    output = ''
    for n, c in hand:
        output += str(n) + c + ' '
    return output

def player_cards_sum(cards):
    result = 0
    for n, _ in cards:
        result += n
    return result


def game_menu():
    deck = create_deck()
    shuffle_deck(deck)
    player_cards = pull_3_cards(deck)
    print(f"Vase karte su: {hand_to_str(player_cards)}")
    in2 = input("Zelite li jos jednu kartu? y/n: ")
    if in2 == 'y':
        player_cards.append(pull_card(deck))
        print(f"Vase karte su: {hand_to_str(player_cards)}")
    opp_result = random.randint(12, 20)
    player_result = player_cards_sum(player_cards)
    print(f"Vas rezultat je {player_result} a protivniov {opp_result}.")
    if player_result > opp_result and player_result <= 20:
        print("Pobijedili ste!")
    else:
        print("Izgubili ste!")


def main():
    while True:
        in1 = input("Zelite li zapoceti igru? y/n: ")
        if in1 == 'n':
            break
        else:
            game_menu()


main()