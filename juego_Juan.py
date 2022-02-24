import random 
op = -1; empates = 0; victorias = 0; derrotas = 0; op = -1 

def menu():
    print('<1> jugar')
    print('<2> resultados')
    print('<3> salir')
if op == 4:
    menu()
while op != 0:
    menu()
    op = int(input('ingrese una opcion: '))
    if op == 1:
        while op != 4:
            print('<1> piedra')
            print('<2> papel')
            print('<3> tijera')
            print('<4> menu principal')
            op = int(input('ingrese eleccion: '))
            num = random.randint(1, 3)
            if op == 1 and op == num:
                print ('empate: ', 'piedra', 'vs', 'piedra')
                empates = empates + 1
            elif op == 1:
                if num == 2:
                    print('pierdo: ', 'piedra', 'vs', 'papel')
                    derrotas = derrotas + 1
                elif num == 3:
                    print('gano: ', 'piedra', 'vs', 'tijera')
                    victorias = victorias + 1
            if op == 2 and op == num:
                print ('empate: ', 'papel', 'vs', 'papel')
                empates = empates + 1
            elif op == 2:
                if num == 3:
                    print('pierdo: ', 'papel', 'vs', 'tijera')
                    derrotas = derrotas + 1
                elif num == 1:
                    print('gano: ', 'papel', 'vs', 'piedra')
                    victorias = victorias + 1
            if op == 3 and op == num:
                print ('empate: ', 'tijera', 'vs', 'tijera')
                empates = empates + 1
            elif op == 3:
                if num == 1:
                    print('pierdo: ', 'tijera', 'vs', 'piedra')
                    derrotas = derrotas + 1
                elif num == 2:
                    print('gano: ', 'tijera', 'vs', 'papel')
                    victorias = victorias + 1
            elif op >= 5:
                print('ingrese una opcion correcta')
    elif op == 2:
        print('empates: ',empates)
        print('victorias ',victorias)
        print('derrotas: ',derrotas)
        print('<3> salir')
        print('<4> menu principal')
        regresar = int(input('ingresar eleccion: '))
        if regresar == 3:
            print('programa finalizado')
            quit()
    elif op == 3:
        print('programa finalizado')
        exit()
    else:
        print('ingrese una opcion correcta')