salary = float(input("Digite el salario bruto: "))

if salary >= 1000000.00:
    print("El salario con impuesto de 10%: ", salary - (salary * 0.10), " colones")
else:
    print("El salario es: ", salary)
