'''
4. napravite program koji ucitava podatke iz prethodno napravljenih datoteka 
te dodatno ispisuje ukupan broj redaka, prosjecan broj koraka (za prvi zadatak), 
odnosno prosjecan postotak pogodaka (za drugi zadatak)
'''
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'lutrija.txt')
    postotci = list()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            postotak = float(line.split('|')[1])
            postotci.append(postotak)
    print(sum(postotci)/len(postotci))

main()