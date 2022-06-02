now = float(input("Digite la cantidad inicial de hormigas: "))
month = int(input("Digite la cantidad de meses a simular: "))


print("Conteo para el mes inicial es de: ",now)
i = 0
while month != 0:
    i += 1
    if now <= 7000:
        now = 0
        print("El hormiguero acabo con las hormigas de la isla en el mes: ", i)
        month = 0
    if 7000 < now <= 28000:
        now = now - 7000
        now = now + (now * 0.40)
        print("La cantidad de hormigas para el mes: ",i," es de: ",now)
        month -= 1
    if now > 28000:
        now = now - 7000
        now = now + (now * 0.31)
        print("La cantidad de hormigas para el mes: ",i," es de: ",now)
        month -= 1
