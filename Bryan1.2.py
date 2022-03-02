#En los siguientes ejercicios, identifique las entradas, procesos y salidas.
#Calcular el mayor de tres números enteros introducidos por teclado.
print("Este sistema le ayudara a reconocer el numero mayor")
#ENTRADA
num1=int(input('Ingrese el primer numero:'))
num2=int(input('Ingrese el segundo numero:'))
num3=int(input('Ingrese el tercer numero:'))
#PROCESO
if num1>=num2 and num1>=num3:
    #SALIDA
    print('El numero mayor es:',num1)
elif num2>=num1 and num2>=num3:
    #SALIDA
    print('EL numero mayor es:',num2)
elif num3>=num1 and num3>=num2:
    #SALIDA
    print('El numero mayor es:',num3)
elif num1==num2==num3:
    #SALIDA
    print('El numero mayor es',num1 or num2 or num3)
