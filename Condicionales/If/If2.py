dat=int(input("Ingrese el año:"))

if dat % 4 == 0 and dat % 100 != 0 or dat % 400== 0:
    print("El año es biciesto")
else:
    print("El año no es biciesto")
