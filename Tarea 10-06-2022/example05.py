state = "s"

while state.lower() == "s":

    año = int(input("Digite el año: "))
    if año % 4 != 0 or (año % 100 == 0 and año % 400 != 0):
        print("No es bisiesto")
    else:
        print("Es bisiesto")

    state = input("Desea continuar: ")