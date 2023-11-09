import numpy as np

def PedirMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: "))
            fila.append(elemento)
        matriz.append(fila)
    matriz_np = np.array(matriz)   
    return matriz_np

def Determinante(matriz, filas, columnas):
    if filas == columnas:
        return np.linalg.det(matriz)
    else:
        return print("Solo se pueden obtener determinantes de matrices cuadradas")

def ProductoEscalar(escalar, matriz):
    matriz2 = matriz[:]
    matriz2 *= escalar
    matriz_escalar = np.array(matriz2) 
    return matriz_escalar

def SumaMatrices(matriz1, matriz2):
    suma = matriz1 + matriz2
    return suma
    
def RestaMatrices(matriz1, matriz2):
    resta = matriz1 - matriz2
    return resta
