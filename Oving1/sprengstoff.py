from sys import stdin

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt 
        self.neste = None 


# Antar at tomme lister aldri vil forekomme
def spor(kubbe):
    hi = kubbe.vekt
    while kubbe.neste != None:
        kubbe = kubbe.neste
        if kubbe.vekt > hi:
            hi = kubbe.vekt
    return hi

# Oppretter lenket liste
def init():
    forste = None
    siste = None
    for linje in stdin:
        forrige_siste = siste
        siste = Kubbe(int(linje))
        if forste == None:
            forste = siste
        else:
            forrige_siste.neste = siste
    print spor(forste)

# Kaller loesningsfunksjonen og skriver ut resultatet
init()

