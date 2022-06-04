limit = int(input("Digite el numero a calcular multiplos:"))

for n in range(1, limit + 1, 1):
    if limit % n == 0:
        print(n)