import numpy as np

class Tablero:
    dim_x = dim_tablero[0]
    dim_y = dim_tablero[1]
    etiq_x = etiquetas_x
    etiq_y = etiquetas_y
    ico_agua = icono_agua
    ico_barco = icono_barco
    
    
    def __init__(self, jugador):
        self.id_jugador = jugador
        self.tablero = [[self.ico_agua for _ in range(10)] for _ in range(10)]
        self.tablero_disparos = [[' ' for _ in range(10)] for _ in range(10)]

    def imprimir_tablero(self):
        print(self.etiq_x)
        for i in range(10):
            print(self.etiq_y[i], end=' ')
            for j in range(10):
                print(self.tablero[i][j], end=' ')
            print()