import random
import numpy as np

# CONSTANTES
dim_tablero = (10, 10, 2)
etiquetas_x = "    A  B   C  D   E  F   G  H   I  J"
etiquetas_y = [" 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10"]
agua = ["A", "🟦"]
barco = ["B", "⬛️"]
tocado = ["T", "🟧"]
fallo = ["F", "⬜️"]


class Tablero:
    dim_x = dim_tablero[0]
    dim_y = dim_tablero[1]
    dim_z = dim_tablero[2]
    etiq_x = etiquetas_x
    etiq_y = etiquetas_y
    agua_c = agua
    barco_c = barco
    tocado_c = tocado
    fallo_c = fallo

    def __init__(self, jugador):
        self.id_jugador = jugador
        self.tablero = np.full((self.dim_x, self.dim_y, self.dim_z), self.agua_c)

    def imprimir_tablero(self):
        print(self.etiq_x)
        for i in range(10):
            print(self.etiq_y[i], end=' ')
            for j in range(10):
                print(self.tablero[i][j][1], end=' ')
            print()

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
                    if not (0 <= nuevo_x < 10 and 0 <= nuevo_y < 10) or self.tablero[nuevo_x][nuevo_y][0] != \
                            self.agua_c[0]:
                        válido = False
                        break
                if válido:
                    for i in range(eslora):
                        self.tablero[x + dirección[0] * i][y + dirección[1] * i] = self.barco_c[1]  # str(eslora)
                    break

    def disparo(self, x, y):
        if self.tablero[x][y][0] == self.agua_c[0]:
            self.tablero[x][y] = self.fallo_c
            return "Agua"
        elif self.tablero[x][y][0] == self.barco_c[0]:
            self.tablero[x][y] = self.tocado_c
            return "Tocado"
        else:
            return "Melon"

    def fin_tablero(self):
        for i in range(self.dim_x):
            for j in range(self.dim_y):
                if self.tablero[i][j][0] == self.barco_c[0]:
                    return False
        return True


def convertir_coordenadas(coordenadas):
    letras = 'ABCDEFGHIJ'
    x = letras.index(coordenadas[0].upper())
    y = int(coordenadas[1:]) - 1
    return x, y


# Función principal del juego
def jugar():
    # Crea la instancia Tablero del Jugador Humano
    nombre_jugador = input("Introduce tu nombre: ")
    tablero_jugador = Tablero(nombre_jugador)

    # Crea la instancia Tablero de la Máquina
    tablero_maquina = Tablero("Máquina")

    # Coloca los barcos en el tablero del jugador humano
    tablero_jugador.colocar_barcos()

    # Coloca los barcos en el tablero de la máquina
    tablero_maquina.colocar_barcos()

    # Bucle principal del juego
    while True:
        # Turno del Jugador Humano
        print(f"\nTurno de {nombre_jugador}:\n")
        tablero_maquina.imprimir_tablero()
        while True:
            coordenadas = input("Introduce las coordenadas de disparo (por ejemplo, A3): ")
            if len(coordenadas) == 2 and coordenadas[0].upper() in 'ABCDEFGHIJ' and coordenadas[1].isdigit():
                x, y = convertir_coordenadas(coordenadas)
                if 0 <= x < 10 and 0 <= y < 10:
                    break
                else:
                    print("Coordenadas fuera del rango. Introduce coordenadas válidas (por ejemplo, A3).")
            else:
                print("Formato de coordenadas incorrecto. Introduce coordenadas válidas (por ejemplo, A3).")

        resultado_disparo = tablero_maquina.disparo(x, y)
        print("\nResultado del disparo:", resultado_disparo)
        if resultado_disparo == "Tocado":
            if tablero_maquina.fin_tablero():
                print(f"\n¡Felicidades {nombre_jugador}! ¡Has hundido todos los barcos de la máquina!")
                break
            print(f"\n¡{nombre_jugador}, vuelves a disparar!")

        # Turno de la Máquina
        print("\nTurno de la Máquina:\n")
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if tablero_jugador.tablero[x][y][0] != tocado[0]:
                break
        resultado_disparo = tablero_jugador.disparo(x, y)
        print("\nResultado del disparo de la Máquina:", resultado_disparo)
        if resultado_disparo == "Tocado":
            if tablero_jugador.fin_tablero():
                print("\n¡La Máquina ha hundido todos tus barcos! ¡Has perdido!")
                break
            print("\n¡La Máquina vuelve a disparar!")

        # Mostrar el tablero de la máquina con los disparos del jugador humano
        print("\nTablero de la Máquina:")
        tablero_maquina.imprimir_tablero()


    # Preguntar al usuario si quiere jugar otra vez
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() != 's':
        print("\n¡Gracias por jugar! ¡Hasta luego!")


# Iniciar el juego
jugar()
