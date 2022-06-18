number1 = int(input("Digite el primer numero: "))
number2 = int(input("Digite el segundo numero: "))

if number1*number1 == number2:
    print("El segundo es el cuadrado exacto del primero")
if number1*number1 > number2:
    print("El segundo es menor que el cuadrado del primero")
if number1*number1 < number2:
    print("El segundo es mayor que el cuadrado del primero")