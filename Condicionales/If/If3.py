#Pedir al usuario la inicial del dia de la semana y mostrar el nombre del dia completo. 
#La letra inicial puede ser mayusculas o minusculas. Usar la x para el miercoles

print("Nota: Para miercoles, ingrese la letra x, por favor")
dia = input("Ingrese la inicial del dia:")

if dia=='L'or dia=='l':
    print("Lunes")
elif dia=='M'or dia=='m':
    print("Martes")
elif dia=='MX'or dia=='Mx'or dia=='mx':
    print("Miercoles")
elif dia=='J'or dia=='j':
    print("Jueves")
elif dia=='V'or dia=='v':
    print("Viernes")
elif dia=='S'or dia=='s':
    print("Sabado")
elif dia=='D'or dia=='d':
    print("Domingo")
else:
    print("Dia Incorrecto.")
