'''
7. nadogradite program iz prethodnog zadatka tako da napravi i konverziju args-a u liste i setove. 
napravite metodu koja ce vrsiti trazene operacije sa setovima. 
neka korisnik preko inputa odluci koju operaciju zeli izvrsiti.
'''

class Converter:
    @staticmethod
    def to_set(*args):
        return set(args)

    @staticmethod
    def to_list(*args):
        return list(args)

    @staticmethod
    def operations(op, set1, set2):
        if op == 'unija':
            return set1 | set2
        if op == 'presjek':
            return set1 & set2
        if op == 'minus':
            return set1 - set2


print(Converter.operations('unija', Converter.to_set(1, 2, 3, 4), Converter.to_set(2, 3, 4, 5)))
print(Converter.operations('presjek', Converter.to_set(1, 2, 3, 4), Converter.to_set(2, 3, 4, 5)))
print(Converter.operations('minus', Converter.to_set(1, 2, 3, 4), Converter.to_set(2, 3, 4, 5)))