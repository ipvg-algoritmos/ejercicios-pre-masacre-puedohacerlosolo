lista = []
while True:
    digito = int(input(f"ingrese un numero: "))
    if digito < 0:
        break
    numero = lista.append(digito)
    print(lista)

lista.sort(reverse=True)
print(f"Tu lista ordenada sería:\n{lista}")