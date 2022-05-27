quantity = int(input("Digite la cantidad de flores: "))
price = float(input("Digite el precio de flores: "))

if (quantity == 3):
    final = (quantity*price) -((quantity*price)*0.10)
else:
    final = (quantity * price)
print("Monto a pagar: ", final)