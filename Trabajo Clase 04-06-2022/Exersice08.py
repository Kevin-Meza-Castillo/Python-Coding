now = float(input("Digite la cantidad inicial de hormigas: "))
month = int(input("Digite la cantidad de meses a simular: "))

i = 0
print("Conteo para el mes inicial es de: ", now)
for month in range(month, 0, -1):
    i += 1
    if now <= 7000:
        now = 7000
        print("El hormiguero acabo con las hormigas de la isla en el mes: ", i)
        month = 0
    if 7000 < now <= 28000:
        now = now + (now * 0.40)
        now = now - 7000
        print("La cantidad de hormigas para el mes: ", i, " es de: ", int(now))
        month -= 1
    if now > 28000:
        now = now + (now * 0.31)
        now = now - 7000

        print("La cantidad de hormigas para el mes: ", i, " es de: ", int(now))
