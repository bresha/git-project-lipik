'''
3. Definirajte klasu Vozilo i dvije podklase Auto i Kamion. Sve klase imaju metodu dobaviVrstu koja ispisuje "Auto" za klasu Auto i "Kamion" za klasu Kamion.
'''

class Vozilo:
    def __init__(self, naziv, km, max_b, cijena):
        self.naziv = naziv
        self.km = km
        self.max_b = max_b
        self.cijena = cijena

    def dobaviVrstu():
        pass

class Auto(Vozilo):
    def __init__(self, naziv, km, max_b, cijena):
        super().__init__(naziv, km, max_b, cijena)

    def dobaviVrstu():
        return 'auto'


class Kamion(Vozilo):
    def __init__(self, naziv, km, max_b, cijena):
        super().__init__(naziv, km, max_b, cijena)

    def dobaviVrstu():
        return 'kamion'