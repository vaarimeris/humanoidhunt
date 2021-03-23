#kasittele kaikkia samaan aikaan
#numerot antaa alotuskoordinaatit, kirjaimet perassa muuttaa koordinaatteja sen verran kun ne sanoo
#kun kaksi koordinaattia paatyy samaan tai vierekkaiseen koordinaattiin, ne yhdistyy
#muuta tiedosto tiedostoksi, jossa jokaisella rivilla on kakiulotteinen lista koordinaatteja
#vaihtele rivien jarjestysta niin kauan, etta loytyy reitti
    #aloita rivista, jossa on S
    #iteroi uusimman listan komponentteja yksi kerrallaan
        #jokaisen kohdalla iteroi lista kerrallaan komponenttien yli
    #kun loytyy lista, jossa on sama tai vierekkainen koordinaatti, lisaa se taas tiedoston viimeiseksi, ja vertaa nyt siihen, kunnes loytyy lista, jossa on F, lopeta
    #tallenna samalla viereisten koodinaattien sijainnit uuteen listaan, kaksiulotteiseen muodossa (rivin numero tiedostossa; koordinaatin paikka listassa)
    #etsi alkuperaisesta tiedostosta S -> A1 -> B1 -> B2 -> C1 -> C2 ... -> ... F
    #lue aina C1 -> C2, riippumatta siita, onko se alkuun vai loppuun.


def make_into_coordinates():
    coordinates = []
    str = open("t3file", "r").read()
    lista1 = str.split('\n')
    #print(lista1)
    n = 0
    while n < len(lista1):
        lista2 = lista1[n].split(' ')
        #print(lista2)
        coordinates.append(lista2)
        n = n + 1

    #print(coordinates[1][1e])
    cods1 = []
    cods2 = []
    m = 0
    while m < len(coordinates):
        lista3 = []
        lista3 = coordinates[m][0].split(',')
        cods1.append(lista3)
        m += 1
        #print(m)
        #m = 0
        #for m in coordinates:
        #print(coordinates[0][1])

        #print(lista3)
        #print(coordinates[110][1])

    #print(cods1)
    k = 0
    while k < len(coordinates):
        lista4 = []
        if len(coordinates[k]) == 1:
            lista4 = ["O"]
            #coordinates[m][0] = lista3
            cods2.append(lista4)
            #print(lista4)
            k += 1
        else:
            #print(coordinates[m][0])
            lista4 = coordinates[k][1].split(',')
            cods2.append(lista4)
            #coordinates[m][1] = lista4
            #print(lista4)
            #print(m)
            #print(coordinates[m][1])
            k += 1
        #print(k)
    #print(len(cods1))
    #print(len(cods2))

    cods3 = []
    #cods3 on se lista, johon kerataan lopuksi
    S_sijainnit = []
    F_sijainnit = []
    X_sijainnit = []
    koordinaattien_sijainti = 0
    while koordinaattien_sijainti < len(cods1):
        vali = []
        k = []
        #__vali = []__ // lista alemmalle kirjaintenlukuloopille, nollataan aina kierroksen lopussa,
        #kun sen arvot on kirjoitettu cods3-listaan
        k.append(int(cods1[koordinaattien_sijainti][0]))
        k.append(int(cods1[koordinaattien_sijainti][1]))
        vali.append(k)
        #vali-listalle lisataan ihan ekaksi alkuperainen koordinaatti
        #print(koordinaattien_sijainti)
        #print(cods1[koordinaattien_sijainti])
        kirjaimen_sijainti = 0
        #print(len(cods2[koordinaattien_sijainti]))
        while kirjaimen_sijainti < len(cods2[koordinaattien_sijainti]):
            #print(cods2[koordinaattien_sijainti][kirjaimen_sijainti])
            #print(kirjaimen_sijainti)
            #print()
            w = []
            #print(int(cods1[koordinaattien_sijainti][1]) - 1)
            if cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "U":
                w.append(int(vali[kirjaimen_sijainti][0]))
                w.append(int(vali[kirjaimen_sijainti][1]) - 1)
                #w = [int(cods1[koordinaattien_sijainti][0]), int(cods1[koordinaattien_sijainti][1]) - 1]
                #vali.append(w)
                #cods1[koordinaattien_sijainti][1] -1 eli vahentaa cods1-listan y-koordinaatista yhden
                #lisaa uuden koordinaatin vali-listaan
                #print(w)

            elif cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "D":
                w.append(int(vali[kirjaimen_sijainti][0]))
                w.append(int(vali[kirjaimen_sijainti][1]) + 1)
                #w = [int(cods1[koordinaattien_sijainti][0]), int(cods1[koordinaattien_sijainti][1]) + 1]
                #vali.append(w)
                #print(w)
            #cods1[koordinaattien_sijainti][1] +1 eli lisaa cods1-listan y-koordinaattiin yhden
            #lisaa uuden koordinaatin vali-listaan

            elif cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "R":
                w.append(int(vali[kirjaimen_sijainti][0]) + 1)
                w.append(int(vali[kirjaimen_sijainti][1]))
                #w = [int(cods1[koordinaattien_sijainti][0]) + 1, int(cods1[koordinaattien_sijainti][1])]
                #vali.append(w)
                #print(w)
                #cods1[koordinaattien_sijainti][0] +1 eli lisaa cods1-listan x-koordinaattiin yhden
                #lisaa uuden koordinaatin vali-listaan

            elif cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "L":
                w.append(int(vali[kirjaimen_sijainti][0]) - 1)
                w.append(int(vali[kirjaimen_sijainti][1]))
                #w = [int(cods1[koordinaattien_sijainti][0]) - 1, int(cods1[koordinaattien_sijainti][1])]
                #vali.append(w)
                #print(w)

            elif cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "s":
                w.append(int(vali[kirjaimen_sijainti][0]))
                w.append(int(vali[kirjaimen_sijainti][1]))
                S_sijainnit.append(w)
                #print("moi")
            #cods1[koordinaattien_sijainti][0] -1 eli vahentaa cods1-listan x-koordinaatista yhden
            #lisaa uuden koordinaatin vali-listaan
            #vali-listalla korvataan cods1[koordinaattien_sijainti]

            elif cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "F":
                print("moi")
                w.append(int(vali[kirjaimen_sijainti][0]))
                w.append(int(vali[kirjaimen_sijainti][1]))
                F_sijainnit.append(w)

            elif cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "x":
                w.append(int(vali[kirjaimen_sijainti][0]))
                w.append(int(vali[kirjaimen_sijainti][1]))
                X_sijainnit.append(w)


            kirjaimen_sijainti += 1
            vali.append(w)
            #print(vali)
            #elifit, jotka loytaa s ja f, tallentaa niitten sijainnit koordinaattina myos


        cods3.append(vali)
        #print(cods3)
        koordinaattien_sijainti += 1
    #print(cods3)
    #print(S_sijainnit)
    #print(F_sijainnit)
    #print(X_sijainnit)
        #
    #print(cods3)
    #s ja f selvitetaan: kysytaan cods2:lta:"missa on s" cods2 vastaa:"index, index", sitten kysytaan cods3:lta"mita tassa on?" se vastaa:"[x, y]


make_into_coordinates()
    #print(cods)
        #print(m)
    #print(coordinates)


#def spin_lines(coordinates):


    #looppi, joka kay lapi tiedoston rivi rivilta

    #poistaa pilkut, splittaa joka rivin listaksi
        #muuttaa jokaisen solun kahden arvon listaksi, frdu:n perusteella

    #lisaa joka listan coordinates-listaan


"""

def iterate(previous list):
    

    return previous_coordinate


def find_those_next_to_this(previous_coordinate, cods3):
    #s on [2,2]

    """



#iteraatio aloitetaan etsimalla joku s
#"etsi mulle kaikki assan viereiset" "ne on: abcde"
#"etsi mulle kaikki a:n viereiset" "ne on:fgh" "etsi kaikki b:n viereiset" jnejnejne
#vertaa kaikkia lotyneita f-listaan
#jos joku on f, lopeta
#f:n indeksi n-ulotteisessa listassa antaa suoraan reitin
#kysyy kayttajalta listana indeksin
#numpylta voi kysya, kuinka moniulotteinen on lista
#(try - exceptIndexError ???)
#while dimension < dimensions
#jos dimensio on olemassa, print mita siihen astisessa dimensio-osoitteessa on
#def main():
 #   make_into_coordinates()
  #  iterate(coordinates)
    #kutsuu find_those_next_to_this
   # arrange_into_list
    #ottaa find_thoselta viereiset, tallentaa ne oikeaan kohtaan isossalistassa


#tehdaan lista, jossa on komponentteina aina [reitin numero, risteavan koordinaatin numero]
#pidetaan ylla jarkea siten, etta "jos tama on jo kaytetty, siirry seuraavaan"
#cods4[reitin numero, risteavan koordinaatin numero]
#cods4[reitin2 numero, edellisen kanssa risteava/viereinen koordinatti]
#pida ylla counter, joka puyorii samaan aikaan iteraation kanssa, ja nain tallentaa f:n indeksin numeoina
#ihan lopuksi funktio, joka luo koordinaateista madon ohjauskaskyt

#test[1][2][3][4][5][6][7]="F"

#def print_reitti():

 #   print()


































