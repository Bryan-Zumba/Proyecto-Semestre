contador=0
for i in range (10):
    for j in range(10):
        contador +=1
        print("i:",i, "j:",j)
        if contador >50:
            break
print("Contador:", contador)
