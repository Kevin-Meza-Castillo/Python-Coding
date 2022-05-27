numLemonade = int(input("Digite la cantidad de limonadas vendidas: "))

utility = (10 * numLemonade) - (5.5 * numLemonade)

pacoUtility = utility * 0.3
luisUtility = utility * 0.3
hugoUtility = utility * 0.4

print("Las ganancias de los chicos son: \nPaco: ", pacoUtility, " colones\n"
                                                                 "Luis: ", luisUtility, " colones\n"
                                                                                        "Hugo", hugoUtility," colones" )
