import sys
n=5
suma=0
menor= sys.maxsize

for i in range(n):
    nota=int(input("Ingrese su nota:"))
    suma += nota
    if nota<menor:
        menor=nota

print("Nota media:",suma/n)
print("Numero menor:", menor)

