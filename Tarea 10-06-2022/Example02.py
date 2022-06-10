init = int(input("Digite el saldo inicial de la cuenta de ahorro: "))

while init > 0:
    withdrawal = float(input("Cual es el monto a retirar: "))

    if withdrawal <= init:
        init-=withdrawal
    else:
        print("Fondos insuficientes")

    print(init)
print("Se terminaron sus fondos")