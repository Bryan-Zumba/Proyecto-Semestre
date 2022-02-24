#Calcular el mayor de tres números enteros introducidos por teclado.

print("Este sistema le ayudara a reconocer el numero mayor")
num1=int(input("Ingrese el primer numero, por favor:"))
num2=int(input("Ingrese el segundo numero, por favor:"))
num3=int(input("Ingrese el tercer numero, por favor:"))

if num1>num2 and num1>num3:
        print('El numero mayor es:',num1)
elif num2>num3 and num2>num1:
        print('El numero mayor es:',num2)
elif num3>num1 and num3>num2:
        print('El numero mayor es:',num3)
elif num1==num2==num3:
    print('Todos los numeros que ha ingresado son iguales')
else:
    print('Existen dos numeros iguales, inserte nuevos numeros :)')
