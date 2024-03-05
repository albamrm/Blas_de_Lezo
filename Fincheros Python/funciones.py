import numpy as np
import random

from variables import*

def colocar_barcos(self):
        barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for eslora in barcos:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                dirección = random.choice(direcciones)
                válido = True
                for i in range(eslora):
                    nuevo_x = x + dirección[0] * i
                    nuevo_y = y + dirección[1] * i
                    if not (0 <= nuevo_x < 10 and 0 <= nuevo_y < 10) or self.tablero[nuevo_x][nuevo_y] != ' ':
                        válido = False
                        break
                if válido:
                    for i in range(eslora):
                        self.tablero[x + dirección[0] * i][y + dirección[1] * i] = self.ico_barco
                    break

def disparar(tablero):
    x = int(input("Introduce la coordenada X para disparar:"))
    y = int(input("Introduce la coordenada Y para disparar:"))
    if tablero[x][y] == "O":
        tablero[x][y] = "X"
        print("Tocado")
    elif tablero[x][y] == "X":
        print("Ya disparaste a esta coordenada anteriormente")
    else:
        tablero[x][y] = "-"
        print("Agua")
    return tablero

def diparar_aleatorio(tablero):
    x = random.randint(0, len(tablero) - 1)
    y = random.randint(0, len(tablero[0]) - 1)
    if tablero[x][y] == "O":
        tablero[x][y] = "X"
        print(f"La máquina ha disparado a la coordenada ({x}, {y}) y le ha dado a uno de tus barcos")
    elif tablero[x][y] == "X":
        print(f"La máquina ha disparado a la corrdenada ({x}, {y}) y ya había disparado ahí anteriormente, ¡que suerte!")
    else:
        tablero[x][y] = "-"
        print(f"Estas de enhorabuena, la máquina ha disparado a la corrdenada ({x}, {y}) y ha dado en el agua.")
    return tablero