num1 = int(input("Digite el primer numero a evaluar: "))
num2 = int(input("Digite el segundo numero a evaluar: "))

if num1 < num2:
    print("El primer numero es el menor: ",num1," > ",num2)
elif num2 < num1:
    print("El segundo numero es el menor: ", num2, " > ", num1)
else:
    print("Son iguales")