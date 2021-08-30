def summe(liste):
    sum = 0
    for i in range(len(liste)):
        sum = sum + liste[i]
        print(sum)
    return sum

def bsp():
    a = 23
    b = 44
    c = a+b
    return c

def median(liste):
    print(liste)
    if type(liste) == list:

        liste = sorted(liste)
        print(liste)
        a = len(liste)//2
        if len(liste) % 2 == 0:
            erg = (liste[a] + liste[a-1])/2


        else:
            erg = liste[len(liste)//2]
    else:
        print("keine Liste")
        print(type(liste))
        exit()
    return erg

#### Hauptprogramm #####
# print("Das Ergebnis ist:", bsp())
# print("Das Ergebnis ist: " + str(bsp()))
liste1 = [2,5,20,12,15,126,]
# erg = summe(liste1)
# print(liste1)
zahl=5
liste =[1,7,3,4,2,6]
print(median(zahl))

