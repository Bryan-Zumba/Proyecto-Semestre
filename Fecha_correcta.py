print("Ingrese la fecha a evaluar")
d=int(input("Ingrese el dia:"))
m=int(input("Ingrese el mes:"))
a=int(input("Ingrese el año:"))

if a>0:
    if m>=1 and m<=12:
        #Meses con 31 dias
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if d>=1 and d<=31:
                print(d,"/",m,"/",a,"es una fecha correcta")
            else:
                print(d,"/",m,"/",a,"es una fecha incorrecta")    
        #Meses con 30 dias
        elif m==4 or m==6 or m==9 or m==11:
            if d>=1 and d<=30:
                print(d,"/",m,"/",a,"es una fecha correcta")
            else:
                print(d,"/",m,"/",a,"es una fecha incorrecta")
        #Mes con 28 dias
        elif m==2:
            if d>=1 and d<=28:
                print(d,"/",m,"/",a,"es una fecha correcta")
            elif  a%4 == 0 and a%100 != 0 or a%400 == 0:
                if d>=1 and d<=29:
                    print(d,"/",m,"/",a,"es una fecha correcta")
                else:
                     print(d,"/",m,"/",a,"es una fecha incorrecta")
            else:
                print(d,"/",m,"/",a,"es una fecha incorrecta")
    else:
        print(d,"/",m,"/",a,"es una fecha incorrecta")
        
else:
    print(d,"/",m,"/",a,"es una fecha incorrecta")