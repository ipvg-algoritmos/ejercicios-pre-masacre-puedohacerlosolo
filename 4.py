lista = []
while True:
    digito = int(input(f"ingrese un numero: "))
    if digito < 0:
        break
    numero = lista.append(digito)
    print(lista)

promedio = sum(lista) / len(lista)
print(f"tu promedio sería {promedio}")