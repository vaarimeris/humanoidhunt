##kasittele kaikkia samaan aikaan
##numerot antaa alotuskoordinaatit, kirjaimet perassa muuttaa koordinaatteja sen verran kun ne sanoo
##kun kaksi koordinaattia paatyy samaan tai vierekkaiseen koordinaattiin, ne yhdistyy
##muuta tiedosto tiedostoksi, jossa jokaisella rivilla on kakiulotteinen lista koordinaatteja
##vaihtele rivien jarjestysta niin kauan, etta loytyy reitti
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
    Ssijainnit = []
    Fsijainnit = []
    Xsijainnit = []
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
                #print("gothere")
                w.append(int(vali[kirjaimen_sijainti][0]) - 1)
                w.append(int(vali[kirjaimen_sijainti][1]))
                #print(w)
                #w = [int(cods1[koordinaattien_sijainti][0]) - 1, int(cods1[koordinaattien_sijainti][1])]
                #vali.append(w)
                #print(w)

            elif cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "S":
                #print("gothere")
                w.append(int(vali[kirjaimen_sijainti][0]))
                w.append(int(vali[kirjaimen_sijainti][1]))
                Ssijainnit.append(w)
                #print(Ssijainnit)

            #cods1[koordinaattien_sijainti][0] -1 eli vahentaa cods1-listan x-koordinaatista yhden
            #lisaa uuden koordinaatin vali-listaan
            #vali-listalla korvataan cods1[koordinaattien_sijainti]

            elif cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "F":
                #print("gothere")
                w.append(int(vali[kirjaimen_sijainti][0]))
                w.append(int(vali[kirjaimen_sijainti][1]))
                Fsijainnit.append(w)
                #print(w)

            elif cods2[koordinaattien_sijainti][kirjaimen_sijainti] == "X":
                #print("gothere")
                w.append(int(vali[kirjaimen_sijainti][0]))
                w.append(int(vali[kirjaimen_sijainti][1]))
                Xsijainnit.append(w)

#TODO selvita miksi s, f, x ei toimi

            vali.append(w)
            kirjaimen_sijainti += 1

            #print(vali)
            #elifit, jotka loytaa s ja f, tallentaa niitten sijainnit koordinaattina myos


        cods3.append(vali)
        koordinaattien_sijainti += 1
        #print(Ssijainnit)
   # print(cods3)
    #print(Ssijainnit)


    return cods3

    #print(S_sijainnit)
    #print(F_sijainnit)
    #print(X_sijainnit)
        #
    #print(cods3)
    #s ja f selvitetaan: kysytaan cods2:lta:"missa on s" cods2 vastaa:"index, index", sitten kysytaan cods3:lta"mita tassa on?" se vastaa:"[x, y]
#make_into_coordinates()

#make_into_coordinates()
    #print(cods)
        #print(m)
    #print(coordinates)


#def spin_lines(coordinates):


    #looppi, joka kay lapi tiedoston rivi rivilta

    #poistaa pilkut, splittaa joka rivin listaksi
        #muuttaa jokaisen solun kahden arvon listaksi, frdu:n perusteella

    #lisaa joka listan coordinates-listaan


def find_those_next_to_this(cods3, previous_coordinate, visited):
    vier =[]
    X_sijainnit = [[127,30],[78,29],[105,44],[0,113],[22,127],[0,108],[0,124],[127,69],[127,68],[0,68]]
    #print(previous_coordinate)
    #print(cods3)
    rivi = 0

    while rivi < len(cods3):
        #print(rivi)
        #print(len(cods3))
        #rivi += 1

        sijainti = 0
        while sijainti < len(cods3[rivi]) - 1:
            #print(cods3[rivi][sijainti])
            #print(y)
            #print(sijainti)
            a = previous_coordinate[0] - cods3[rivi][sijainti][0]
            #print(cods3[rivi][sijainti])
            b = previous_coordinate[1] - cods3[rivi][sijainti][1]
            #print(previous_coordinate)
            #print(cods3[rivi][sijainti][0])
            #print(abs(a))
            #print(previous_coordinate[1])
            #print(cods3[rivi][sijainti][1])
            #print(abs(b))
            #print("a on oikeasti", a)

            if (abs(a) + abs(b)) < 2:
                #print(abs(a) + abs(b))
                #if b == 0 or 1 or -1:

                if cods3[rivi][sijainti] not in visited:
                    #print(cods3[rivi][sijainti])
                    vier.append(cods3[rivi][sijainti])
                    visited.append(cods3[rivi][sijainti])
                    #print(visited)

                elif cods3[rivi][sijainti] in X_sijainnit:
                    visited.append(cods3[rivi][sijainti])
                    #print(visited)
                #print(abs(previous_coordinate[0] - cods3[x][y][0]))

            #print(sijainti)

            sijainti += 1
        rivi = rivi + 1
    #print(vier)
    #print(x)
    return vier

#find_those_next_to_this()


""" 
                    if cods3[x][y] not in visited: #problem probably here
                        vier.append(cods3[x][y])
                        #print(cods3[x][y])
                        visited.append(cods3[x][y])
                        #print(vier)
                        
                    elif cods3[x][y] in X_sijainnit:
                    visited.append(cods3[x][y])


"""



 #print(vier)
#TODO debugaa taa koko funktio, en usko etta toimii
#ei tee mitaan???




#def make_paths(biglist, previous_coordinate, viereiset):

#   for

#in biglist store all paths
#go through each path, by picki
#call next to this to find all nodes of

#lista = []
#try index(previous_coordinate)

#except ValueError:
 #lista.append(viereiset)

def write_as_UDLR(reitti):
    #reitti = [[2, 2], [1, 3], [1, 2], [2, 8]]
    UDLR_reitti = []
    UDLR_reitti.append("S")
    p = 1
    while p < len(reitti):
        #print(len(reitti))
        #print(reitti[p-1][1])
        if reitti[p][0] - reitti[p-1][0] == 1:
            UDLR_reitti.append("R")
            #print(reitti[p])

        if reitti[p][0] - reitti[p-1][0] == -1:
            UDLR_reitti.append("L")

        if reitti[p][1] - reitti[p-1][1] == 1:
            UDLR_reitti.append("D")

        if reitti[p][1] - reitti[p-1][1] == -1:
            UDLR_reitti.append("U")

        p += 1
    #UDLR_reitti.append("F")
    #print(UDLR_reitti)

    return UDLR_reitti

#write_as_UDLR(reitti)

#iteraatio aloitetaan etsimalla joku s // s on 2,2
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


def main():
    cods3 = []
    S_sijainnit = [2,2]
    F_sijainnit = [[105,15],[105,12],[105,13],[111,15],[122,15],[105,6],[119,15],[105,4],[113,15],[105,10],[117,15]]
    X_sijainnit = [[127,30],[78,29],[105,44],[0,113],[22,127],[0,108],[0,124],[127,69],[127,68],[0,68]]
    cods3 = make_into_coordinates()
    #print(cods3)
    previous_coordinate = []
    biglist = []
    visited = [[2,2]]
    reitti = []
    UDLR_reitti = []
    #thing = []
    biglist.append(S_sijainnit)
    #print(biglist)
    #biglist.append(thing)
    #print(biglist[0][-1])
    #previous_coordinate.append(biglist[n])
    #print(previous_coordinate)
    #print(biglist[n])

    previous_coordinate = biglist[0]
    viereiset = find_those_next_to_this(cods3, previous_coordinate, visited)
    #print(viereiset)
    h = 0
    while h < len(viereiset):
        #print(viereiset)
        newnew = []
        new = biglist[0][:]
        newnew.append(new)
        newnew.append(viereiset[h])
        #biglist.append(new)
        #print(newnew)
        biglist.append(newnew)
        #print(biglist)
        #print(new)
        h += 1

    n = 1

    #print(biglist)
    #TODO everything below this is probs bs, do something abt it
    while n < len(biglist):
        previous_coordinate = biglist[n][-1]
        #print(biglist[n])
        #print(previous_coordinate)
        viereiset = find_those_next_to_this(cods3, previous_coordinate, visited)
        #print(viereiset)
        k = 0
        new = []
        while k < len(viereiset):
            new = biglist[n][:]
            #print(new)
            new.append(viereiset[k])
            biglist.append(new)
            #print(new)
            #new *= 0

            if viereiset[k] in F_sijainnit:
                reitti = new
                #print(reitti)
                UDLR_reitti = write_as_UDLR(reitti)
                print(UDLR_reitti)
            k += 1

        n += 1
    #print(biglist[4])

    #reitti = [[2, 2], [1, 3], [1, 2], [2, 8]]

    #why's the info not going through???


     #???? wut toimiikot -- no ei

main()

#sailo jokainen reitti biglistin osasena. on helpompi pitaa hanskassa montaa melkein-kopiota, kun riveta rakentamaan
#moniulotteista listaa eleganssin vuoksi





#while n < len(viereiset):
 #eli loopin sisalle for n in enumerate tan output
#   vier = find_those_next_to_this(cods3, viereiset[n])


#  ok = 1
# while ok == 1:
 #    ok = arrange_into_list(biglist, viereiset)
     #tama on nyt se tarkistus, arrange palauttaa 1 jos viereisissa ei ole f
 #n += 1

 #laita tama looppiin, jossa tata kutsutaan aina uudestaan ja uudestaan sen listan enumeratella, jonka se on palauttanut
 #se looppi alkaa 2,2:sesta,
 #??????


#ottaa find_thoselta viereiset, tallentaa ne oikeaan kohtaan isossalistassa
#vertaa f-listaan ja x-listaan.
#jos kuuluu x-listaan, kohtelee sita kuin olisi jo aikaisemmin kaytetty, eli ei lisaa sita isoonlistaan.
#jos kuuluu f-listaan, tekee halytyksen ja pysayttaa kaiken, palauttaa f:n indeksin isossalistassa

#BFS, jossa kasitellaan viereisten koordinaattien listoja,
#vai DFS, jossa kaydaan yksi kerrallaan niin syvalle kuin paasee,ja sen jalkeen peruutetaan?
#BFS, koska jos otan DFS, niin pitaa ottaa huomioon kaikki ne, jotka loppuu, mutta joilla on viereissia
#saattaa tulla kierteita



#tehdaan lista, jossa on komponentteina aina [reitin numero, risteavan koordinaatin numero]
#pidetaan ylla jarkea siten, etta "jos tama on jo kaytetty, siirry seuraavaan"
#cods4[reitin numero, risteavan koordinaatin numero]
#cods4[reitin2 numero, edellisen kanssa risteava/viereinen koordinatti]
#pida ylla counter, joka puyorii samaan aikaan iteraation kanssa, ja nain tallentaa f:n indeksin numeoina
#ihan lopuksi funktio, joka luo koordinaateista madon ohjauskaskyt

#test[1][2][3][4][5][6][7]="F"

#def print_reitti():

#   print()





