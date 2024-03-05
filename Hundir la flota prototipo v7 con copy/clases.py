# clases.py
import numpy as np
from variables import TAMANO_TABLERO, BARCOS
import random

class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.dimensiones = TAMANO_TABLERO
        self.barcos = BARCOS
        self.tablero = np.zeros((self.dimensiones, self.dimensiones), dtype=int)
        self.tablero_impactos = np.zeros((self.dimensiones, self.dimensiones), dtype=int)
        self.barco_vidas = {nombre: eslora for nombre, eslora in self.barcos.items()}
        self.posiciones_barcos = {}  # Diccionario para almacenar las posiciones de los barcos
        self.coordenadas_disparadas = set()  # Conjunto para almacenar las coordenadas ya disparadas

    def inicializar_tablero(self):
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for nombre, eslora in self.barcos.items():
            posiciones_barco = []
            while True:
                x = random.randint(0, self.dimensiones - 1)
                y = random.randint(0, self.dimensiones - 1)
                dirección = random.choice(direcciones)
                válido = True
                for i in range(eslora):
                    nuevo_x = x + dirección[0] * i
                    nuevo_y = y + dirección[1] * i
                    if not (0 <= nuevo_x < self.dimensiones and 0 <= nuevo_y < self.dimensiones) or self.tablero[nuevo_x][nuevo_y] != 0:
                        válido = False
                        break
                if válido:
                    for i in range(eslora):
                        self.tablero[nuevo_x - dirección[0] * i][nuevo_y - dirección[1] * i] = 1
                        posiciones_barco.append((nuevo_x - dirección[0] * i, nuevo_y - dirección[1] * i))
                    break
            self.posiciones_barcos[nombre] = posiciones_barco

    def disparo_coordenada(self, x, y):
        if (x, y) in self.coordenadas_disparadas:
            print("¡Coordenada ya disparada! Patán, elige otra.")
            return

        impacto = False
        for nombre_barco, posiciones_barco in self.posiciones_barcos.items():
            for pos in posiciones_barco:
                if pos == (x, y):
                    self.barco_vidas[nombre_barco] -= 1
                    if self.barco_vidas[nombre_barco] == 0:
                        for pos in posiciones_barco:
                            self.tablero_impactos[pos[0], pos[1]] = 3  # Marcar el barco como hundido en el tablero de impactos
                        print(f"¡Felicidades, has hundido el barco {nombre_barco}!")
                    else:
                        self.tablero_impactos[x, y] = 2  # Marcar el barco como tocado en el tablero de impactos
                        print("¡Tocado!")
                    impacto = True
                    break
            if impacto:
                break
        if not impacto:
            self.tablero_impactos[x, y] = 1  # Marcar agua en el tablero de impactos
            print("¡Agua!")
        
        self.coordenadas_disparadas.add((x, y))




            
    def obtener_nombre_barco(self, x, y):
        for nombre, eslora in self.barcos.items():
            if self.id_jugador == "Jugador":
                if np.sum(self.tablero[x:x+eslora, y]) == eslora:
                    return nombre
            else:
                if np.sum(self.tablero[x:x+eslora, y]) == eslora:
                    return nombre
                
# Otras funciones necesarias para el juego
    def imprimir_tablero_con_barcos(self, es_tablero_maquina=False):
        if es_tablero_maquina:
            nombre_jugador = "Flota enemiga"
            tablero = self.tablero_impactos
        else:
            nombre_jugador = self.id_jugador
            tablero = self.tablero
            
        print(f"\nTablero de {nombre_jugador}:")
        # Encabezado de columnas con valores de los ejes x
        print("  ", end="")
        for i in range(self.dimensiones):
            print(f"{i} ", end="")
        print()
        
        for i in range(self.dimensiones):
            # Encabezado de filas con valores del eje y
            print(f"{i} ", end="")
            for j in range(self.dimensiones):
                if tablero[i][j] == 0:
                    print("~ ", end="")
                elif tablero[i][j] == 1:
                    print("O ", end="")
                else:
                    print("X ", end="")
            print()
