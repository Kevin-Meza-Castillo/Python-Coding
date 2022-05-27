name = input("Digite el nombre del cliente: ")
age = int(input("Digite los años de fidelidad: "))
pay = float(input("Digite el monto a recargar: "))

if (1 < age < 3) & (2000 <= pay < 3800):
    total = pay * 2
    print("Estimado(a) cliente ", name, " su recargada es por un monto total de ", total,
          " colones, se le ha aplicado la promoción de recarga doble")
elif (3 <= age < 5) & (3800 <= pay <= 5000):
    total = pay * 3
    print("Estimado(a) cliente ", name, " su recargada es por un monto total de ", total,
              ' colones, se le ha aplicado la promoción de recarga triple')
elif (age >= 5):
    total = pay * 3
    print("Estimado(a) cliente ", name, " su recargada es por un monto total de ", total,
          ' colones, se le ha aplicado la promoción de recarga triple')
else:
    print("Estimado cliente", name, "el monto de su recarga es de: ", pay)
