limit = int(input("Cual es el factorial de: "))

prod = 1

for limit in range(limit, 0, -1):
    prod = prod * limit
print("El factorial es: ", prod)
