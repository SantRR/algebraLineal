import funciones

filas = int(input("Ingrese el número de filas de las matrices: "))
columnas = int(input("Ingrese el número de columnas de las matrices: "))
escalar = float(input("Ingrese el escalar: "))

print("Ingrese la primera matriz:")
matriz_A = funciones.PedirMatriz(filas, columnas)

print("Ingrese la segunda matriz:")
matriz_B = funciones.PedirMatriz(filas, columnas)

resultado_suma = funciones.SumaMatrices(matriz_A, matriz_B)
resultado_resta = funciones.RestaMatrices(matriz_A, matriz_B)
resultado_escalar = funciones.ProductoEscalar(escalar, matriz_A)
resultado_determinante = funciones.Determinante(matriz_A)

print(resultado_suma)
print("\n", resultado_resta)
print("\n", resultado_escalar)
print("\n", resultado_determinante)
