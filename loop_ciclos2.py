
contador_positivos=0
contador_negativos=0
contador_neutros=0


for i in range(5):
    numbers=int(input("Ingrese el numero:"))
    if numbers>0:
        contador_positivos+=1
    elif numbers<0:
        contador_negativos+=1
    else:
        contador_neutros+=1

print("Total positivos:", contador_positivos)
print("Total negativos:", contador_negativos)
print("Total neutros:", contador_neutros)