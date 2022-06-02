limit = int(input("Digite el numero a calcular multiplos:"))

flag = 1

while flag <= limit:
    if limit % flag == 0:
        print(flag)
    flag += 1
