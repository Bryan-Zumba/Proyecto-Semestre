#En los siguientes ejercicios, 
# identifique las entradas, procesos y salidas.

#Escribir un programa que solicite un valor entero al usuario
# y determine si es positivo o negativo.

#ENTRADA
num=int(input("Ingrese un numero entero, por favor:"))
#PROCESO
if num>0:
    #SALIDA
    print("El numero que ha ingresado es positivo.")
elif num<0:
    #SALIDA
    print("El numero que ha ingresado es negativo.")
else:
    #SALIDA
    print('El 0 no es positivo ni negativo.')
exit