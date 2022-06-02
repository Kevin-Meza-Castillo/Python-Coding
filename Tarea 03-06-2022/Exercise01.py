limit = int(input("Digite el numero limite:"))

flag = 1

while flag != limit:
    if flag % 2 == 0:
        print(flag)
    flag += 1
