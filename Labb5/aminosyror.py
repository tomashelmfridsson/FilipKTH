# Aminosyror

import re
import sys

# Skapa en klass för aminosyrorna
class Aminosyra:
    def __init__(self, code, name, grupp, vikt):
        self.code = code
        self.name = name
        self.grupp = grupp
        self.vikt = vikt
    def __repr__(self):
        return f"code: {self.code} name: {self.name}, grupp: {self.grupp}, vikt: {self.vikt}"
    
# Skapa en klass med sekvens av aminosyror
class Sekvens:
    def __init__(self, sekvens, vikt):
        self.sekvens = sekvens
        self.vikt = vikt
    
    def __repr__(self):
        return f"sekvens: {self.sekvens}, vikt: {self.vikt}"
    
    def get_vikt(self):
        return self.vikt

# Läs in från filen aminosyror.txt och skapa upp objekt av klassen Aminosyra
def las_in_aminosyror(filnamn):
    aminosyror = []
    try:
        with open(filnamn, 'r') as fil:
            for rad in fil:

                rad= rad.strip()
                delar = re.split(r'\s+', rad)
                print(delar) 
                if len(delar) == 4:
                    code = delar[0].strip()
                    name = delar[1].strip()
                    grupp = delar[2].strip()
                    vikt = float(delar[3])
                    aminosyra = Aminosyra(code, name, grupp, vikt)
                    aminosyror.append(aminosyra)
        return aminosyror
    except FileNotFoundError:
        print(f"Filen {filnamn} hittades inte.")
        sys.exit()

aminosyrorLista= las_in_aminosyror('aminosyror.txt')
for aminosyra in aminosyrorLista:
    print(aminosyra)

def skrivut_aminosyror():
    for aminosyra in aminosyrorLista:
        print(aminosyra)    

def skapa_sekvens():
    sekvens_input = input("Ange en sekvens av aminosyror (t.ex. ACGT): ").strip().upper()
    sekvens = input('Ange en sekvens av aminosyror (t.ex. ACGT): ')
    vikt = 0
    for bokstav in sekvens:
        for aminosyra in aminosyrorLista:
            if aminosyra.code == bokstav:
                vikt += aminosyra.vikt
    print(f'Sekvensen {sekvens} har en total vikt av {vikt}')
    sekvensLista.append(Sekvens(sekvens, vikt))

def skrivut_sekvenser():
    sekvensLista.sort(key=Sekvens.get_vikt, reverse=True)
    for sekvens in sekvensLista:
        print(sekvens)

def main():
    val = ''
    while val != '4':
        print('')
        print('Välj ett av följande:')
        print('1 - Lista alla aminosyror')
        print('2 - Spara en sekvens av aminosyror (peptid)')
        print('3 - Lista alla sekvenser sorterare i viktordning')
        print('4 - Avsluta')
        val = input('Ditt val: ')

        if val == '1':
            skrivut_aminosyror()
        elif val == '2':
            skapa_sekvens()
        elif val == '3':
            skrivut_sekvenser()


aminosyrorLista= las_in_aminosyror('aminosyror.txt')
sekvensLista = []
main()

