flag=0
day=int(input("Ingrese el dia: "))
month=int(input("Ingrese el mes: "))
year=int(input("Ingrese el annio: "))
if(year%4==0):
    if(year%100!=0 or year%400==0):
        leap=1
    else:
        leap=0
else:
    leap=0
if(leap==1):
    if(month==2):
        if(day>=1 and day<=28):
            day=day+1
            #day+=1 es lo mismo que lin 15
        #elif(day==29):
        else:
            if(day==29):
                day=1
                month+=1
            else:
                print("fecha invalida, dia incorrecto")
                flag=1
    else:
        if(month==4 or month==6 or month==9 or month==11):
            if (day >= 1 and day <= 29):
                day = day + 1
            else:
                if (day == 30):
                    day = 1
                    month += 1
                else:
                    print("fecha invalida, dia incorrecto")
                    flag = 1
        else:
            if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
                if(month==12 and day==31):
                    year+=1
                    month=1
                    day=1
                else:
                    if (day >= 1 and day <= 30):
                        day = day + 1
                    else:
                        if (day == 31):
                            day = 1
                            month += 1
                        else:
                            print("fecha invalida, dia incorrecto")
                            flag = 1
            else:print("fecha incorrecta, mes invalido")
            flag=1
else:
    if (month == 2):
        if (day >= 1 and day <= 27):
            day = day + 1
        else:
            if (day == 28):
                day = 1
                month += 1
            else:
                print("fecha invalida, dia incorrecto")
                flag = 1
    else:
        if (month == 4 or month == 6 or month == 9 or month == 11):
            if (day >= 1 and day <= 29):
                day = day + 1
            else:
                if (day == 30):
                    day = 1
                    month += 1
                else:
                    print("fecha invalida, dia incorrecto")
                    flag = 1
        else:
            if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                if (month == 12 and day == 31):
                    year += 1
                    month = 1
                    day = 1
                else:
                    if (day >= 1 and day <= 30):
                        day = day + 1
                    else:
                        if (day == 31):
                            day = 1
                            month += 1
                        else:
                            print("fecha invalida, dia incorrecto")
                            flag = 1
            else:
                print("fecha incorrecta, mes invalido")
                flag = 1
if(flag==0):
    print(day,"-",month,"-",year)