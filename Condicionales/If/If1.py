temp=int(input("Ingrese la temperatura:"))

if temp<0:
    print("Solido")
elif temp>=0 and temp<=100:
    print("Liquido")
elif temp>100:
    print("Gaseoso")
