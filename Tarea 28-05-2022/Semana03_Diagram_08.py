cost = float(input("Digite el valor del automovil: "))
tax = cost * 0.30
utility = cost * 0.10
finalCost = tax + cost

print("El costo del automovil es de: $", finalCost, ", la comision del vendedor es de: $", utility,
      "y el impuesto de: $", tax)
