number1 = int(input("Digite el primer numero: "))
number2 = int(input("Digite el segundo numero: "))
number3 = int(input("Digite el tercer numero: "))

if number1 > number2:
    if(number1 < number3):
        print("El numero mayor es el tercera:", number3)
    else:
        print("El numero mayor es el primero:",number1)
else:
    if number2 > number3:
        print("El numero mayor es el segundo:", number2)
    else:
        print("El numero mayor es el tercero:", number3)