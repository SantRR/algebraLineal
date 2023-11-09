import numpy as np

def pedir_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: "))
            fila.append(elemento)
        matriz.append(fila)
    matriz_np = np.array(matriz)   
    return matriz_np


def producto_escalar(escalar, matriz):
    matriz *= escalar
    matriz_escalar = np.array(matriz) 
    return matriz_escalar

def suma_matrices(matriz1, matriz2):
    suma = matriz1 + matriz2
    return suma
    
def resta_matrices(matriz1, matriz2):
    resta = matriz1 - matriz2
    return resta
