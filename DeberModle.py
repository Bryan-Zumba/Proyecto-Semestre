# Determinar en que estado está el agua en función de su temperatura. 
# Si es negativa el estado será sólido, 
# si es menor que 100 será líquido y si es mayor que 100 será gas. 
# Pedir al usuario el valor de la temperatura.

temp=int(input("Ingrese la temperatura:"))

if temp<0:
    print("Solido")
elif temp>=0 and temp<=100:
    print("Liquido")
elif temp>100:
    print("Gaseoso")
exit