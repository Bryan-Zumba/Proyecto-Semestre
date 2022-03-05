#Calcular media aritmética y suma total de "n" elementos

n= int(input("Ingrese el valor de N:"))
suma=0
for i in range(n):
    nota=int(input("Ingrese su nota:"))
    suma= suma+nota

print("Suma total:", suma)
media_a =suma/n
print("Media aritmetica:", media_a)
