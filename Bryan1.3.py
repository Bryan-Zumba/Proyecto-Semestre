#num1=int(input('Ingrese el primer numero:'))
#num2=int(input('Ingrese el segundo numero:'))
#num3=int(input('Ingrese el tercer numero:'))


num1=1
num2=2
num3=3

if num1<num2:
    num1,num2=num2,num1

if num1<num3:
    num1,num3=num3,num1

print("El numero mayor es:",num1)