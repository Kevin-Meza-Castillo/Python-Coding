salaryBrut = float(input("Digite el salario bruto del empleado: "))
salaryTax = float(input("Digite el impuesto del empleado en %: "))

salaryNet = salaryBrut - (salaryBrut*(salaryTax/100))

print("El salarios neto del empleado es: ",salaryNet)
