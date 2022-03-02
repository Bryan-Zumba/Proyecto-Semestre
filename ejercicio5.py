#Pedir al usuario un valor. Si el valor es positivo,
#Pedir un segundo valor y calcular la suma, resta y producto de
#ambos. Mostrar los resultados por pantalla

num=int(input("Ingrese su numero:"))

if num>0:
    num2=int(input('Ingrese un segundo numero:'))

    Suma=num+num2
    print('La suma de los dos numeros es',Suma)

    Resta=num-num2
    print('La resta de los dos numeros es',Resta)
    
    Producto=num*num2
    print('El producto de los dos numeros es:',Producto)

else: print('El numero que ha ingresado es negativo')
print('...')