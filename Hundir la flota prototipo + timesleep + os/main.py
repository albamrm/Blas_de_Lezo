# main.py
import os
import time

from clases import Tablero
from funciones import imprimir_tablero, generar_coordenadas_aleatorias

def main():
    print("¡Saludos, marinero intrépido! \nSoy Blas de Lezo y Olavarrieta, nacido en Pasajes, Guipúzcoa, el 3 de febrero de 1689. \nA lo largo de mi vida, he surcado los mares y enfrentado numerosas batallas, \nquedando marcado por las heridas de guerra que adornan mi figura: \nun ojo tuerto, un brazo inmovilizado y una pierna arrancada. \nA pesar de estas adversidades, he demostrado ser un estratega formidable, \nsiendo considerado uno de los mejores almirantes de la historia de la Armada Española.")
    time.sleep(8)
    
    print("\nHoy necesito tu ayuda, \nte invito a participar en una emocionante batalla naval, \ndonde la astucia y la estrategia serán nuestras mejores armas. \nAntes de adentrarnos en esta aventura marítima,")
    time.sleep(5)
    nombre_jugador = input("\n¿Con qué nombre quieres que te recuerde la historia? ")
    
    print(f"\nBienvenido, {nombre_jugador}, preparemonos para la batalla!")
    time.sleep(2)
    
    print("\nEl campo de batalla está listo para la acción. \nAhora, es momento de posicionar nuestros barcos en las aguas revueltas. \nNuestras fuerzas y las del enemigo son parejas. \nCada bando cuenta con: \n4 barcos de 1 posición de eslora \n3 barcos de 2 posiciones de eslora \n2 barcos de 3 posiciones de eslora \n1 barco de 4 posiciones de eslora")
    time.sleep(8)
    
    print("\nConfía en mi criterio para colocar los barcos. \nTu responsabilidad es hundir la flota enemiga, \nasí que céntrate en dirigir los disparos de nuestra artillería")
    time.sleep(5)
    
    os.system('cls')  

    # Inicializamos los tableros de ambos jugadores
    tablero_jugador = Tablero(id_jugador=nombre_jugador)
    tablero_maquina = Tablero(id_jugador="Flota enemiga")
    tablero_jugador.inicializar_tablero()
    tablero_maquina.inicializar_tablero()

     # Imprimir los tableros con los barcos colocados
    tablero_jugador.imprimir_tablero_con_barcos()
    #tablero_maquina.imprimir_tablero_con_barcos()
    
    time.sleep(3)
    os.system('cls')

    while True:
        # Turno del jugador humano
        print("¡Es tu turno! Atizales:")
        imprimir_tablero(tablero_jugador.tablero_impactos)
        x, y = map(int, input("Introduce las coordenadas separadas por comas (x, y). \nRecuerda números entre el 0 y el 9 según muestra el tablero: ").split(","))
        tablero_maquina.disparo_coordenada(x, y)
        
        # Verificamos si el jugador ha perdido
        if sum(tablero_jugador.barco_vidas.values()) == 0:
            print("¡Hemos perdido! La Flota enemiga ha ganado.")
            break
        
        # Turno de la máquina
        print("Turno de la Flota enemiga:")
        x, y = generar_coordenadas_aleatorias()
        print(f"La Flota enemiga dispara a las coordenadas {x}, {y}.")
        tablero_jugador.disparo_coordenada(x, y)
        
        # Verificamos si la máquina ha perdido
        if sum(tablero_maquina.barco_vidas.values()) == 0:
            print("¡Hemos ganado! La Flota enemiga ha sido eliminada. ¡Bravo!")
            break

        time.sleep(3)
        os.system('cls')

if __name__ == "__main__":
    main()
