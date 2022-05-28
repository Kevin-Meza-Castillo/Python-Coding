lado1 = int(input("Ingrese el lado A :"))
lado2 = int(input("Ingrese el lado B :"))
lado3 = int(input("Ingrese el lado C :"))

sumaLado12 = lado1+lado2
sumaLado13 = lado1+lado3
sumaLado23 = lado2+lado3

if (sumaLado12 > lado3) & (sumaLado13 > lado2) & (sumaLado23 > lado1):
    print("Es un triangulo")

else:
    print("No es un triangulo")
