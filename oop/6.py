'''
6. napravite klasu po zelji. neka jedna metoda prima args, a druga kwargs. u glavnom potprogramu predajte odgovarajuce vrijednosti te ih ispisite.
'''

class Nesto:
    @staticmethod
    def nestoargs(*args):
        for i in args:
            print(i)

    @staticmethod
    def nestokwargs(**kwargs):
        for i in kwargs.keys():
            print(kwargs[i])


Nesto.nestoargs(1, 2, 3, 4)
Nesto.nestokwargs(a = 5, b = 6, c= 7)