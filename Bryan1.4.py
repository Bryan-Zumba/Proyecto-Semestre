#Calcular el mayor de 4 numeroas ingresados por el teclado
num1=90
num2=9
num3=6
num4=5
num5=4 

if num1<num2:
    num1,num2=num2,num1
if num1<num3:
    num1,num3=num3,num1
if num1<num4:
    num1,num4=num4,num1
if num1<num5:
    num1,num5=num5,num1
if num2<num3:
    num2,num3=num3,num2
if num2<num4:
    num2,num4=num4,num2
if num2<num5:
    num2,num5=num5,num2
if num3<num4:
    num3,num4=num4,num3
if num3<num5:
    num3,num5=num5,num3
if num4<num5:
    num4,num5=num5,num4

print(num1)
print(num2)
print(num3)
print(num4)
print(num5)