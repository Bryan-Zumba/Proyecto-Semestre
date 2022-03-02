print("Ingrese la fecha a evaluar, para identificar su signo zodiaco")
dia=int(input("Ingrese el dia de nacimiento:"))
mes=int(input("Ingrese el mes de nacimiento:"))
if mes == 12 and dia >= 22 or mes == 1 and dia <= 20: 
    print("Su signo es Capricornio")
elif mes == 1 and dia >= 21 or mes == 2 and dia <=19:
    print("Su signo es Acuario")
elif mes == 2 and dia >= 20 or mes == 3 and dia <=20:
    print("Su signo es Piscis")
elif mes == 3 and dia >= 21 or mes == 4 and dia <=19:
    print("Su signo es Aries")
elif mes == 4 and dia >= 20 or mes == 5 and dia <=20:
    print("Su Signo es Tauro")
elif mes == 5 and dia >= 21 or mes == 6 and dia <=21:
    print("Su Signo es Geminis")
elif mes == 6 and dia >= 22 or mes == 7 and dia <=21:
    print("Su Signo es Cancer")
elif mes == 7 and dia >= 22 or mes == 8 and dia <=21:
    print("Su Signo es Leo")
elif mes == 8 and dia >= 22 or mes == 9 and dia <=22:
    print("Su signo es Virgo")
elif mes == 9 and dia >= 23 or mes == 10 and dia <=22:
    print("Su signo es Libra")
elif mes == 10 and dia >= 23 or mes == 11 and dia <=21:
    print("Su signo es Escorpio")
elif mes == 11 and dia >= 22 or mes == 12 and dia <=21:
    print("Su signo es Sagitario")