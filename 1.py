import random

lista = [random.randint(1, 100) for i in range(10)]

print(f"Lista: {lista}")

while True:
    selección = input("Ingresa un número: ")
    if selección.isdigit():
        numero = int(selección)
        if numero in lista:
            posición = lista.index(numero)
            print(f"Encontrado, posición: {posición}")
            break 
        else:
            print("Numero no está en la lista")
    else:
        print("No es numero")
