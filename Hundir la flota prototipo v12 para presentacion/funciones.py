# funciones.py
from variables import TAMANO_TABLERO
import random

'''def imprimir_tablero(tablero, id_jugador):
    print(f"Tablero del {id_jugador}:")
    
    # Encabezado de columnas con valores de los ejes x
    print("  ", end="")
    for i in range(len(tablero)):
        print(f"{i} ", end="")
    print()
    
    # Encabezado de filas con valores del eje y y contenido del tablero
    for i in range(len(tablero)):
        print(f"{i} ", end="")
        for j in range(len(tablero[i])):
            if tablero[i][j] == 0:
                print("~", end=" ")
            elif tablero[i][j] == 1:
                print("O", end=" ")
            elif tablero[i][j] == 2:
                print("X", end=" ")
            else:
                print("E", end=" ")  # E para errores
        print()'''

def generar_coordenadas_aleatorias():
    return random.randint(0, TAMANO_TABLERO - 1), random.randint(0, TAMANO_TABLERO - 1)
