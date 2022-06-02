blockComplete = int(input("Digite 1 si lleva bloque completo, de lo contrario ingrese cualquier otro valor numerico: "))
if blockComplete != 1:
    print("Lo sentimos, ud no puede optar por la beca!!!")
else:
    note1 = float(input("Ingrese la nota de la primera materia: "))
    note2 = float(input("Ingrese la nota de la segunda materia: "))
    note3 = float(input("Ingrese la nota de la tercera materia: "))
    note4 = float(input("Ingrese la nota de la cuarta materia: "))
    promGrades = (note1 + note2 + note3 + note4) / 4
    assistence = int(input("Digite 1 si fue asistente el cuatri pasado, de lo contrario digite cualquier otro valor: "))
    if assistence == 1:
        gradeAssistent = input("Digite su calificacion de asistente: ")
        if gradeAssistent.upper() == "C":
            print("Lo sentimos, no califica para la beca")
        else:
            if promGrades >= 85 and (gradeAssistent.upper() == "A" or gradeAssistent.upper() == "B"):
                print("Felicidades, usted puede optar por una beca")
            else:
                print("Lo sentimos, no califica para la beca")
    else:
        if promGrades >= 90 and note1 >= 80 and note2 >= 80 and note3 >= 80 and note4 >= 80:
            print("Felicidades, usted puede optar por una beca")
        else:
            print("Lo sentimos, no califica para la beca")
