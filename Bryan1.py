#Escribir un programa que solicite un valor entero al usuario
# y determine si es positivo o negativo.

num=int(input('Ingrese un numero entero:'))

if num>0:
    print('El numero es positivo')
elif num<0:
    print('El numero es negativo')
else:
    print('El 0 no es positivo ni negativo')