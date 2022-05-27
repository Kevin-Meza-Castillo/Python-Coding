initHour = int(input("Ingrese la hora de entrada formato militar: "))
finalHour = int(input("Ingrese la hora de salida formato militar: "))
price = float(input("Ingrese el precio por hora de la tarifa: "))

if (finalHour - initHour)-8 != 0:
    utility = (8 * price) + ((price*1.5)*((finalHour - initHour)-8))
else:
    utility = (finalHour - initHour) * price

print("La ganancia del dia es de: ", utility, " colones")
