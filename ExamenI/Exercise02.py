print("Bienvenido al sistemas de calculo de promedios")
students = int(input("Digite la cantidad de estudiantes: "))
approve = 0
reprobate = 0
sufficiency = 0

for x in range(0, students):

    grade1 = float(input("Digite la primer nota: "))
    grade2 = float(input("Digite la segunda nota: "))
    grade3 = float(input("Digite la primer nota: "))
    promedio = (grade1 * 0.20 + grade2 * 0.30 + grade3 * 0.50)
    print(promedio)

    if promedio >= 60:
        if promedio < 70:
            print("El estudiante de realizar ampliacion")
            sufficiency+=1
        else:
            print("El estudiante aprobo")
            approve+=1
    else:
        print("Perdio el curso")
        reprobate+=1

print("La cantidad de estudiante que ganaron el curso son: ",approve)
print("La cantidad de estudiante que perdieron el curso son: ",reprobate)
print("La cantidad de estudiante que van a suficiencia el curso son: ",sufficiency)