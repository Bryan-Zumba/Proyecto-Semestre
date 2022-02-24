#Calcular el mayor de dos numeros enteros introducidos por el teclado
#entrada
num1= int(input('Ingreso num 1:'))

num2= int(input('Ingreso num 2:'))

#proceso
if num1 > num2:
    #salida
    print('El numero mayor es:',num1)
elif num2> num1:
    print('El numero mayor es:',num2)
else:
    print('Los numeors son iguales')
