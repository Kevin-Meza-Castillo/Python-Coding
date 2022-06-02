exams = int(input("Digite el numero de examenes: "))
i = 0
prom = 0
addiction = 0

while exams != i:
    grade = int(input("Digite la nota del examen :"))
    addiction += grade
    i += 1
prom = addiction / exams

if prom >= 60:
    if prom < 70:
        print("El estudiante de realizar ampliacion")
    else:
        print("El estudiante aprobo")
else:
    print("Perdio el curso")
