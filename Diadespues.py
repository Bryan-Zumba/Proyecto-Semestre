#Dada la fecha de hoy,
#Calcular la fecha del dia siguiente
#Suponer que el año no es bisiesto

dia=int(input("Ingrese el dia:"))
mes=int(input("Ingrese el mes:"))
año=int(input("Ingrese el año:"))

if mes<=0 or mes>12 or dia<=0 or dia>31 or año<0: # Casos de fechas incorrectas
    print("Fecha incorrecta")
elif mes in [1, 3, 5, 7, 8, 10, 12]: # Meses con 31 dias
    if dia==31 and mes==12: 
        año=año+1  
        mes=1
        dia=1
    elif dia==31 and mes!=12: 
        mes=mes+1  
        dia=1    
    else: # si no es diciembre, ni 31
        dia=dia+1 
    print("La fecha siguiente es {}/{}/{}".format(dia,mes,año))
elif mes in [4, 6, 9, 11] and dia<=30: #Meses con 30 dias
    if dia==30: 
        mes=mes+1 
        dia=1
    else: # sólo se incrementa al día
        dia=dia+1 
    print("La fecha siguiente es {}/{}/{}".format(dia,mes,año))
elif mes==2 and dia<=28: #Febrero en año no bisiesto tiene 28 dias
    if dia==28: 
        mes=mes+1 
        dia=1
    else: # Si no es 28, sólo se incrementa el día
        dia=dia+1 
    print("La fecha siguiente sera: {}/{}/{}".format(dia,mes,año))
else: 
    print("Fecha incorrecta, elegir otra fecha a evaluar, por favor")