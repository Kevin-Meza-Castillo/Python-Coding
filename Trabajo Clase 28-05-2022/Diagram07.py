#Tablas de multiplicar

suma=0
contador = 1
tablaNumero = int(input(("Introduzca el numero de la tabla a multiplicar, el numero debe de ser en un rango del 1 al 10: ")))
print("Tabla de multiplicar del", tablaNumero)
while(contador <=12):
    suma = suma+tablaNumero
    contador+=1
    print(suma)