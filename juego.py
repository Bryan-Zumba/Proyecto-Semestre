import random
op=1;Empates=0;Victorias=0;Derrotas=0

while op !=0:
    print("Bienvenido a ♦ Piedra, Papel o Tijera ♦")
    print()
    print('<1> Jugar')
    print('<2> Resultados')
    print('<3> Salir')
    print()
    op=int(input("Seleccione una opción:"))
    
    if op==1:
        while op !=4:
            print()
            print("<1> Piedra")
            print("<2> Papel")
            print("<3> Tijera")
            print("<4> Regresar al Menú Principal")
            print()
            op=int(input("Ingrese su elección:"))
            num=random.randint(1,3)
            print()

            if op==1:
                if op==num:
                    print("Empate:","Piedra","vs","Piedra")
                    Empates=Empates+1
                elif num==2:
                    print("Pierdo:", "Piedra","vs", "Papel")
                    Derrotas=Derrotas+1
                elif num==3:
                    print("Gano:", "Piedra","vs", "Tijera")
                    Victorias=Victorias+1

            elif op==2:
                if op==num:
                    print("Empate:","Papel","vs","Papel")
                    Empates=Empates+1 
                elif num==3:
                    print("Pierdo:", "Papel","vs", "Tijera")
                    Derrotas=Derrotas+1
                elif num==1:
                    print("Gano:", "Papel","vs", "Piedra")
                    Victorias=Victorias+1

            elif op==3:
                if op==num:
                    print("Empate:","Tijera","vs","Tijera")
                    Empates=Empates+1 
                elif num==1:
                    print("Pierdo:", "Tijera","vs", "Piedra")
                    Derrotas=Derrotas+1
                elif num==2:
                    print("Gano:", "Tijera","vs", "Papel")
                    Victorias=Victorias+1
            
            elif op>=5:
                print("Introduzca una opción permitida")

    elif op==2:
        
        print()
        print("Mostrando resultados:")
        print("Victorias:", Victorias)
        print("Derrotas:", Derrotas)
        print("Empates:", Empates)
        print()
    
    elif op ==3:
        print()
        print("Programa finalizado...")
        quit()
    else:
        print()
        print("Ingrese una opción válida...")