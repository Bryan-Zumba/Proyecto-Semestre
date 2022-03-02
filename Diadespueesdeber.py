#Dada la fecha de hoy,
#Calcular la fecha del dia siguiente
#Suponer que el año no es bisiesto

dia=int(input("Ingrese el dia:"))
mes=int(input("Ingrese el mes:"))
año=int(input("Ingrese el año:"))

def fecha_dia_siguiente(agnio, mes, dia):
    bisiesto = False

    if agnio % 400 == 0:
        bisiesto = True
    elif agnio % 4 == 0:
        bisiesto = True

    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
    elif mes == 2:
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        dias_mes = 30

    if dia < dias_mes:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            agnio += 1
        else:
            mes += 1

    return (agnio, mes, dia)


print(fecha_dia_siguiente(2020, 1, 15))
print(fecha_dia_siguiente(2020, 1, 31))
print(fecha_dia_siguiente(2020, 2, 28))
print(fecha_dia_siguiente(2020, 12, 31))