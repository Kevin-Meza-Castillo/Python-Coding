year = int(input("Ingrese el annio: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Es un annio bisiesto")
else:
    print("No es un annio bisiesto")
