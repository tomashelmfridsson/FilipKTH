# Laboration 4

# Innehåll: Klass & objekt, instansvariabler och instansmetoder, konstruktor, self. Listor av objekt.

# Ni ska i denna uppgift läsa in data om (europeiska) länder från en fil och beräkna total population för de som är landlåsta där ett landlåst land definieras som ett land utan tillgång till hav.

# En körning ska se ut så här (grönt är programmets utmatning):
# I Europa har följande länder inte tillgång till hav:
# Vatican City
# San Marino
# Liechtenstein
# Switzerland
# Luxembourg
# Andorra
# Moldova
# Czech Republic
# Slovakia
# Hungary
# Serbia
# Austria
# Macedonia
# Belarus
# Totalt bor i dessa 14 länder 66608875 människor.

 
# Filen finns under Filer/Laborationer och heter "europa.txt".

# Krav på lösningen:

# Inläsningen från fil görs i en separat funktion.
# Strukturen ska lagras som en lista av objekt där varje objekt innehåller instansvariabler för:

# nationens namn <str>
# folkmängden <int>
# om det är landlåst <bool>




# Skapar en klass
class Land:
    def __init__(self,namn,folkmangd,landLast): # Konstruktor med 2 inparametrar folkmängd och landlåst
        self.namn = namn
        self.folkmangd = folkmangd
        self.landLast = landLast

# Läs in filen och sortera upp allt innehåll, returnera en lista med länder i classen Land    
def filinlasning(filnamn):
    with open(filnamn, mode='r', encoding='utf-8') as infil:
        landInformationText = infil.read()
    landInformationLista = landInformationText.split('\n') # Får en lista med varje land i eget element spearerade med tabbar och komma?
    #print(landInformationLista)

    # Tvätta rent från tab och strukturera upp informationen i en lista
    listaMedAllaLanderUtanTab=[] # Ny lista för att spara alla rensade lander
    for landinfo in landInformationLista: 
        landListaMedTab = landinfo.split(',') #Skapar en lista, tyvärr följer massa tabbar med
        landListaUtanTab = []         
        for landMedTab in landListaMedTab:
            landListaUtanTab.append(landMedTab.strip())  # Lägger till i en ny lista utan tabbar
        listaMedAllaLanderUtanTab.append(landListaUtanTab) # Lägger till i den tvättade lista
        #print(landListaUtanTab = [] )

    # skapa en lista med class
    landListaMedTypClassenLand = []    
    for index,land in enumerate(listaMedAllaLanderUtanTab):   # JAg behöver veta att jag index för att sortera bort rubriken
        if index > 0:  # Vill inte ha med rubrikraden, eventuellt detta tidigare
            #print(land)
            namn = land[0]
            invanare = int(land[2])
            if land[3] == 'N': 
                landLast = False
            else:
                landLast = True
            nyttLand = Land(namn,invanare,landLast) #skapar en instans av klassen Land 
            landListaMedTypClassenLand.append(nyttLand) #lägger till i listan som typen classen Land
    return landListaMedTypClassenLand


def main():
    landlista=filinlasning('europa.txt')
    print('I Europa har följande länder inte tillgång till hav:')
    summaInvannare=0
    antalLander=0
    for land in landlista:
        #print(land.namn,land.folkmangd,land.landLast)
        if land.landLast: 
            print(land.namn)
            antalLander += 1
            summaInvannare += land.folkmangd
    print(f'Totalt bor i dessa {antalLander} länder {summaInvannare} människor.')
main()

