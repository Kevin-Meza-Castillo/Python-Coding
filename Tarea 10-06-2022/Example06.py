import random
machines = int(input("Digite la cantidad de maquinas: "))
ip = int(input("Digite el indice de productividad: "))
exc = 0
good = 0
worse = 0

for n in range(0,machines):
    productivity = 0
    for week in range(0,4):
        productivity += random.randint(0, 1500)
    if productivity == ip:
        good += 1
    if productivity > ip:
        exc +=1
    else:
        worse +=1
    print("La maquina numero: ", n ," tiene una productividad de ", productivity )

print("Cantidad de maquinas con produccion excelente: ",exc )
print("Cantidad de maquinas con produccion buena: ",good )
print("Cantidad de maquinas con produccion mala: ",worse )