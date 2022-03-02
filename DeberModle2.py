#Un año es bisiesto si es divisible por 4 y no es por 100, o si es divisible por 400. 
# Escribe un programa que lea un año y devuelva si es bisiesto o no.

dat=int(input("Ingrese el año:"))

if dat % 4 == 0 and ((dat % 100 != 0) or (dat % 400== 0)):
    print("El año es biciesto")
else:
    print("El año no es biciesto")









