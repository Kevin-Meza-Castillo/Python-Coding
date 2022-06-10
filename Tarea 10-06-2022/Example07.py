import random

factories = int(input("Digite la cantidad de fabricas: "))

prodFactPre = 0
factJuly = 0
nameFact = ""
facExc = ""

for f in range(0, factories):
    prodYear = 0
    nameFact = input("Digite el nombre la fabrica: ")
    for month in range(0, 12):
        prodMonth = random.randint(0, 7000000)
        if (month == 6):
            if (prodMonth > 3000000):
                factJuly += 1
                print("July")
        prodYear += prodMonth

    print("La fabrica ", nameFact, " tiene una produccion de: ", prodYear, " al año")
    if prodFactPre < prodYear:
        facExc = nameFact
        prodFactPre = prodYear
print("La fabrica que mas unidades fabrica es: ",facExc," con ",prodFactPre," unidades")
print("Cantidad e empresa que elaboraron mas de 3 000 000 de unidades en julio: ",factJuly)