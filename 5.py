matriz = [["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]]
for i in range(3):
    for x in range(3):
        sipo = matriz[i][x] = input(f"Inserte numero fila {i} y  columna {x}: ")
print(matriz[0])
print(matriz[1])
print(matriz[2])
positivos = 0
negativos = 0
neutros = 0

for i in range(3):
    for x in range(3):
        if int(matriz[i][x]) > 0:
            positivos += 1
        elif int(matriz[i][x]) < 0:
            negativos += 1
        else:
            neutros += 1
print(f"hay {positivos} positivos")
print(f"hay {negativos} negativos")
print(f"hay {neutros} neutros")

diagonal1 = int(matriz[0][0]) + int(matriz[1][1]) + int(matriz[2][2])
diagonal2 = int(matriz[2][0]) + int(matriz[1][1]) + int(matriz[0][2])
if diagonal1 >= diagonal2:
    print(f"la diagonal principal es mayor\n{diagonal1} > {diagonal2}")
elif diagonal1 <= diagonal2:
    print(f"la diagonal secundaria es mayor\n{diagonal1} < {diagonal2}")
else:
    print(f"las diagonales valen lo mismo\n{diagonal1} = {diagonal2}")
