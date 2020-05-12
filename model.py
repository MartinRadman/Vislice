stevilo_dovoljenih_napak = 10

pravilna_crka = '+'
ponovljena_crka = 'O'
napacna_crka = '-'

zmaga = 'W'
poraz = 'x'


class Igra:
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo.lower()
        self.crke = [c.lower() for c in crke]

    def napacne_crke(self):
        napacne = [c for c in self.crke if c not in self.geslo]
        return napacne

    def pravilne_crke(self):
        pravilne = [c for c in self.crke if c not in self.geslo]
        return pravilne

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False
        return True

    def poraz(self):
        return len(self.stevilo_napak()) > stevilo_dovoljenih_napak

    def pravilni_del_gesla(self):
        uganjene = ''
        for c in self.geslo:
            if c in self.crke:
                uganjene += c
            else:
                uganjene += '_'
        return uganjene

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        '''Metoda ugibaj, ki spremeni stanje igre, glede na uporavnikovo ugibanje.'''
        crka = crka.upper()

        if crka in self.crke():
            return ponovljena_crka

        self.crke.append(crka)

        # Preverimo stanje igre po ugibu
        if crka in self.geslo:
            if self.zmaga():
                return zmaga
            else:
                return pravilna_crka
        else:
            if self.poraz():
                return poraz
            else:
                return napacna_crka
