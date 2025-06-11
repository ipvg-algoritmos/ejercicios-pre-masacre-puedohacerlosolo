vocales = ["a", "e", "i", "o", "u"]

frase = input("dame una frase o palabra: ")
sipo = frase.lower()
nopo = sipo.replace(" ","")

cantidadvocales = 0
cantidadconsonantes = len(nopo)


print(nopo)
for letra in nopo:
    if letra in vocales:
        cantidadvocales += 1
        cantidadconsonantes -= 1
print(f"vocales: {cantidadvocales}")
print(f"consonantes: {cantidadconsonantes}")
