#El ciclo for ejecuta un bloque de 

mascotas= ['gatos', 'perros', 'gatos', 'peces', 'perros', 'perros']

for i in mascotas:
    print(i)

contadorgatos=0
contadorperros=0
contadorpeces=0
for i in mascotas:
    if i=="gatos":
        contadorgatos=contadorgatos + 1
    elif i in "perros":
        contadorperros=contadorperros+1
    elif i in "peces":
        contadorpeces=contadorpeces+1

print("El numero de gatos es:",contadorgatos)
print("El numero de perros es:",contadorperros)
print("El numero de peces es:",contadorpeces)