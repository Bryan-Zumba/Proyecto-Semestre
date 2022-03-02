salario= int(input('ingresar salario:'))
antiguedad=int(input('ingresar antiguedad:'))

if antiguedad < 1:
    utilidad=salario* 0.5
elif antiguedad >=1 and antiguedad <2: 
    utilidad=salario*0.7
elif antiguedad >=2 and antiguedad<5:
    utilidad=salario*0.10
elif antiguedad >=5 and antiguedad<10:
    utilidad=salario*0.15
elif antiguedad >=10:
    utilidad=salario*0.20
print('la utilidad deacuerdo a:',antiguedad,'años de servicio es:',utilidad)
print('tu salario total con la utilidad es',salario+utilidad)