country = input("Digite el nombre del pais: ")
sickness = int(input("Digite la cantidad de enfermos totales: "))
deads = int(input("Digite la cantidad de muertes totales: "))

mortality = (deads/sickness)*100

print("La tasa de mortalidad del pais: ",country, "es de: ",mortality,"%")