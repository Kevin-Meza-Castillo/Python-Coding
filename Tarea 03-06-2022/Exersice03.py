limit = int(input("Cual es el factorial de: "))

prod = 1

while limit != 0:
    prod = prod * limit
    limit -= 1
print("El factorial es: ", prod)
