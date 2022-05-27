nameProduct = input("Digite el nombre del producto: ")
priceProduct = float(input("Digite el precio unitario del producto: "))

totalPrice = priceProduct + (priceProduct * 0.13)

print("El producto: ", nameProduct, "tiene un precio final de :", totalPrice, " colones")
