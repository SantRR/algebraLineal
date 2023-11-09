from paquete_ibero_al import ibero_al as AL

filas = int(input("Ingrese el número de filas de las matrices: "))
columnas = int(input("Ingrese el número de columnas de las matrices: "))
escalar = float(input("Ingrese el escalar: "))

print("Ingrese la primera matriz:")
matriz_A = AL.PedirMatriz(filas, columnas)

print("Ingrese la segunda matriz:")
matriz_B = AL.PedirMatriz(filas, columnas)

resultado_suma = AL.SumaMatrices(matriz_A, matriz_B)
resultado_resta = AL.RestaMatrices(matriz_A, matriz_B)
resultado_determinante = AL.Determinante(matriz_A, filas, columnas)
resultado_escalar = AL.ProductoEscalar(escalar, matriz_A)

print(resultado_suma)
print("\n", resultado_resta)
print("\n", resultado_determinante)
print("\n", resultado_escalar)
