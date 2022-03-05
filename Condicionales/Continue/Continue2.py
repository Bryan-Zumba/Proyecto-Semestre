#Se excluye un supuesto dia no laborable, en este caso el día 18
for n in range(31):
    if n==18:
        continue
    print(n,"Día Laborable")
