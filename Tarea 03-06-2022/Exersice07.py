quantityGroup = int(input("Cantidad de grupos de programacion: "))
quantityEst = int(input("Cantidad de estudiantes: "))
exams = int(input("Digite el numero de examenes: "))
win = 0
lose = 0
draft = 0

while quantityGroup != 0:
    print("Grupo",quantityGroup)
    j = 0
    while quantityEst != j:
        i = 0
        prom = 0
        addiction = 0
        print("Nota del estudiante: ", j + 1)
        while exams != i:
            grade = int(input("Digite la nota del examen :"))
            addiction += grade
            i += 1
        prom = addiction / exams
        print(prom)
        if prom >= 60:
            if prom < 70:
                print("El estudiante de realizar ampliacion")
                draft += 1
            else:
                print("El estudiante aprobo")
                win += 1
        else:
            print("Perdio el curso")
            lose += 1

        j += 1
    quantityGroup -= 1

print("Los estudiantes que ganaron el curso fueron: ",win)
print("Los estudiantes que van ampliacion del curso fueron: ",draft)
print("Los estudiantes que perdieron el curso fueron: ",lose)