name = input("Digite el nombre de usuario: ")
lastname = str(input("Digite el apellido del usuario: "))
dateBorn = int(input("Ingrese el año de nacimiento: "))
height = float(input("Digite su altura: "))

age = 2022 - dateBorn

print("Hola", name, lastname, "tu edad es", age, "y naciste en el año", dateBorn)
