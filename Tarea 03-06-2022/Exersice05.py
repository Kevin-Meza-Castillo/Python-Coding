exams = int(input("Digite el numero de examenes: "))
i = 0
prom = 0
addiction = 0

while exams != i:
    grade = int(input(f"Digite la nota del examen {i+1}: "))
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
