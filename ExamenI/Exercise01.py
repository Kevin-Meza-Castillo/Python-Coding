print("Bienvenido al sistemas de calculo de salario semanal")
horas = float(input("Indique la cantidad de horas laboradas: "))
tarifaNormal = float(input("Indique el valor de hora normal: "))
tarifaExtra = float(input("Indique el valor de hora extra: "))

if horas >= 0 and tarifaNormal >= 0 and tarifaExtra >= 0:
    if horas <= 35:
        salario = horas * tarifaNormal
    else:
        salario = (tarifaNormal*35) +(tarifaExtra*(horas-35))
    print("El salario del empleado es ",salario)
else:
    print("Existe un error horas, tarifa normal o tarifa extra son iguales a 0 o menores")