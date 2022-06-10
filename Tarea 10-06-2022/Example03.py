state = "n"
days = 0
caps = 0
while state.lower() == "n":
    caps += int(input("¿Cuantos capitulos leyo el dia de hoy?: "))
    days += 1
    state = input("¿Termino el libro?: ")

print("Felicidades, usted leyo un libro de ",caps," capitulos en ",days," dias")
