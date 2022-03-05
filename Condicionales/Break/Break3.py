#No acepta números negativos, añadiendo el break el programa finalizará cuando se digite números mayores o iguales a 5
num = 0
while num >= 0:
    num = int(input('Introduce un número: '))
    if num>=5:
        break
