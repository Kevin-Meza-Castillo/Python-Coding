number = int(input("Digite un numero positivo: "))
count = 0
for n in range(1, number+1):
    if number % n == 0:
        count += 1
if count <= 2:
    print("El numero: ",number," es primo")
else:
    print("El numero: ", number, " no es primo")