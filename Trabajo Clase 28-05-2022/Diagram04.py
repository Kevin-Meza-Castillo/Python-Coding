cantidadN=int(input("Ingrese la cantidad de numeros que desea sumar: "))
contador=1
multiplicacion=1
suma=0

while(contador<=cantidadN):
    numero=int(input("Ingrese un numero: "))
    if numero%2==0:
        suma=suma+numero
    else:
        multiplicacion= multiplicacion*numero

    contador+=1
print("El resultado de la suma es: ", suma)
print("El resultado de la multiplicacion es de: ", multiplicacion)