exams = int(input("Digite el numero de examenes: "))
prom = 0
addiction = 0

for n in range(0, exams, 1):
    grade = int(input(f"Digite la nota del examen {n}: "))
    addiction += grade
prom = addiction / exams

if prom >= 60:
    if prom < 70:
        print("El estudiante de realizar ampliacion")
    else:
        print("El estudiante aprobo")
else:
    print("Perdio el curso")
