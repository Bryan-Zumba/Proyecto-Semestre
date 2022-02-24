#Dada la fecha de hoy,
#Calcular la fecha del dia siguiente
#Suponer que el año no es bisiesto

dia=int(input("Ingrese el dia:"))
mes=int(input("Ingrese el mes:"))
año=int(input("Ingrese el año:"))


print("Su fecha ingresada es:",dia,"/", mes,"/", año)

# meses en 31: 1,3,5,7,8,10,12
# meses en 30: 4,6,9,11
# meses en 28 o 29: 2

ultimo_dia=28
if año % 4 == 0 and ((año % 100 != 0) or (año % 400== 0)):
    ultimo_dia=29

if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes ==8 or mes == 10 or mes == 12:
    if dia == 31:
        dia=1
        if mes !=12:
            mes += 1
        elif mes == 12:
            año += 1
            mes=1
    else:
        dia +=1
elif mes == 4 or mes == 6 or mes ==9 or mes ==11:
    if dia==30:
        dia=1
        mes+= 1
    else:
        dia+=1
elif mes==2:
    if dia== ultimo_dia:
        dia=1
        mes+=1
    else:
        dia+=1

print("La fecha siguiente es:", dia,"/", mes,"/", año)