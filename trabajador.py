trab=float(input("Indique los años que lleva trabajando en la empresa:"))
salario=float(input("Indique su salario:"))

if trab>0 and trab<1:
    util=salario*0.05
    print("Su utilidad es:",util)
    print("Total a recibir:", salario+util)

elif trab>=1 and trab<2:
    util=salario*0.07
    print("Su utilidad es:",util)
    print("Total a recibir:", salario+util)

elif trab >=2 and trab <5:
    util=salario*0.10
    print("Su utilidad es:",util)
    print("Total a recibir:", salario+util)

elif trab >=5 and trab <10:
    util=salario*0.15 
    print("Su utilidad es:",util)
    print("Total a recibir:", salario+util)

elif trab>=10:
    util=salario*0.20 
    print("Su utilidad es:",util)
    print("Total a recibir:", salario+util)

else:
    print("No puede haber trabajado 0 años o menos tiempo del mismo :)")

