#El continue hará que en los números establecidos no se ejecute el print
j=0
for i in range(10):
    j+=2
    print("i:",i,"j:",j)
    if j >=2 and j<=10:
        continue
    print("El valor de j:",j)
