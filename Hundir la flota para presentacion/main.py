# main.py
import os
import time
from variables import TAMANO_TABLERO, BARCOS
from clases import Tablero
from funciones import generar_coordenadas_aleatorias

def main():
    print("¡Saludos, marinero intrépido! \nSoy Blas de Lezo y Olavarrieta, nacido en Pasajes, Guipúzcoa, el 3 de febrero de 1689. \nA lo largo de mi vida, he surcado los mares y enfrentado numerosas batallas, \nquedando marcado por las heridas de guerra que adornan mi figura: \nun ojo tuerto, un brazo inmovilizado y una pierna arrancada. \nA pesar de estas adversidades, he demostrado ser un estratega formidable, \nsiendo considerado uno de los mejores almirantes de la historia de la Armada Española.")
    time.sleep(8)
    
    print("\nHoy necesito tu ayuda, \nte invito a participar en una emocionante batalla naval, \ndonde la astucia y la estrategia serán nuestras mejores armas. \nAntes de adentrarnos en esta aventura marítima,")
    time.sleep(5)
    nombre_jugador = input("\n¿Con qué nombre quieres que te recuerde la historia? ")
    
    os.system('cls')  

    print(f"\nBienvenido, {nombre_jugador}, preparemonos para la batalla!")
    time.sleep(2)
    
    print("\nEl campo de batalla está listo para la acción. \nAhora, es momento de posicionar nuestros barcos en las aguas revueltas. \nNuestras fuerzas y las del enemigo son parejas. \nCada bando cuenta con: \n4 barcos de 1 posición de eslora \n3 barcos de 2 posiciones de eslora \n2 barcos de 3 posiciones de eslora \n1 barco de 4 posiciones de eslora")
    time.sleep(5)
    
    print("\nConfía en mi criterio para colocar los barcos. \nTu responsabilidad es hundir la flota enemiga, \nasí que céntrate en dirigir los disparos de nuestra artillería")
    time.sleep(5)

    print(f"\n¡ATENTO, {nombre_jugador}! En un mar embrabecido ~~~ veras \nlos disparos fallidos como O, \nlos aciertos como X y \nlos barcos hundidos como H.")
    time.sleep(5)
    
    os.system('cls')  

    # Inicializamos los tableros de ambos jugadores
    tablero_jugador = Tablero(id_jugador=nombre_jugador)
    tablero_maquina = Tablero(id_jugador="Flota enemiga")
    tablero_jugador.inicializar_tablero()
    tablero_maquina.inicializar_tablero()

     # Imprimir los tableros con los barcos colocados
    tablero_jugador.imprimir_tablero_con_barcos()
    tablero_maquina.imprimir_tablero_con_barcos()
    
    time.sleep(10)
    os.system('cls')

    while True:
        # Turno del jugador humano
        print("\nTus disparos")
        tablero_maquina.imprimir_tablero()
        print("\nDisparos del enemigo")
        tablero_jugador.imprimir_tablero()
        print("¡Es tu turno! Atizales:")

        try:
            # He hecho unas modificaciones para ver los tableros de disparos de ambos jugadores cada vez que hacemos una jugada y así tener una visual del juego
            x, y = map(int, input("\nIntroduce las coordenadas separadas por comas (x, y). \nRecuerda números entre el 0 y el 9 según muestra el tablero: ").split(","))
            
            # Verificar si las coordenadas están dentro del rango permitido
            if not (0 <= x < TAMANO_TABLERO and 0 <= y < TAMANO_TABLERO):
                print("¡Coordenadas fuera del rango! Deben estar entre 0 y 9.")
                continue  # Vuelve al inicio del bucle

            # Disparar en las coordenadas introducidas
            tablero_maquina.disparo_coordenada(x, y)

            # Verificamos si el jugador ha perdido
            if sum(tablero_jugador.barco_vidas.values()) == 0:
                print("\n¡Hemos perdido! La Flota enemiga ha ganado.")
                break

            # Turno de la máquina
            print("\nTurno de la Flota enemiga:")
            time.sleep(3)  # Añado un timesleep para hacer como que la máquina piensa
            x, y = generar_coordenadas_aleatorias()
            print(f"La Flota enemiga dispara a las coordenadas {x}, {y}.")
            tablero_jugador.disparo_coordenada(x, y)

            # Verificamos si la máquina ha perdido
            if sum(tablero_maquina.barco_vidas.values()) == 0:
                print("\n¡Hemos ganado! La Flota enemiga ha sido eliminada. ¡Bravo!")
                break

            time.sleep(3)
            os.system('cls')
            
        except ValueError:
            print("¡Error, zoquete! Debes introducir números enteros separados por comas.")
            time.sleep(3)


if __name__ == "__main__":
    main()
