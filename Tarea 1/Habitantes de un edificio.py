
puertas = int(input("Introduce numero de puertas: "))
pisos = int(input("Introduce numero de pisos: "))

matriz = []
for i in range(puertas):
    matriz.append([0] * pisos)

mayor = None  # Mayor valor encontrado hasta el momento.
puerta = 0      # puerta de `mayor`
piso = 0   # piso de `mayor`
for i in range(puertas):
    for j in range(pisos):
        matriz[i][j] = int(input("puerta {}, piso {} : ".format(i + 1, j + 1)))
        if mayor is None: # Inicializamos mayor aqui.
            mayor = matriz[i][j] - 1
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            puerta = i
            piso = j

print("La puerta con el numero mayor de habitantes es: ")
print(mayor)
print("Puerta", puerta + 1, ", Piso", piso + 1)
print("La matriz es:")
print(matriz)
