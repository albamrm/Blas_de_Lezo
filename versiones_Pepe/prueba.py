import numpy as np
import pandas as pd
import time
import random


def marcador(yo, enemigo):
    if len(yo.strip()) <= 1 or yo.strip().lower() in ["me da igual", "no importa", "quit"]:
        yo = "Blas de Lezo"
    if len(enemigo.strip()) <= 1 or enemigo.strip().lower() in ["me da igual", "no importa", "quit"]:
        enemigo = "Edward Vernon"
    
    dic_info = {
        'jugadores': [yo, enemigo], 
        'Tiros acertados': [0, 0],
        'Tiros recibidos': [0, 0],
        'Tiros fallados': [0, 0],
        'Tiros totales': [0, 0]
    }
    tabla_info_pd = pd.DataFrame(dic_info)
    tabla_info_pd.set_index('jugadores', inplace=True)
    return tabla_info_pd

yo = input("¿Cómo te llamas? (pulsa una sola letra para nombre por defecto.) ")
enemigo = input("¿Cómo se llama tu enemigo? (pulsa una sola letra para nombre por defecto.) ")

def selector_tamaño():
    while True:
        x = input("¿DE QUÉ TAMAÑO DESEA SU TABLERO? El tablero será cuadrado. ") 
        if not x.isdigit():
            print("INGRESE SOLO VALORES NUMÉRICOS POSITIVOS")
        else:
            x = int(x)

            if x == 0:
                print("JO JO JO... MUY GRACIOSO")
            elif x < 7:
                print("EL TAMAÑO DEL TABLERO DEBE SER COMO MÍNIMO DE 7") 
            elif x < 23:
                print("SU TABLERO DE ", x, "FILAS Y ", x, "COLUMNAS SE ESTÁ CREANDO.\n")
                return x          
            elif x == 23:
                print("WOW... TE GUSTA EL JUEGO")
                print("SU TABLERO DE ", x, "FILAS Y ", x, "COLUMNAS SE ESTÁ CREANDO.\n")
                return x
            elif x > 99: 
                
                print("WOW ESO ES IMPOSIBLE AMIGO")
            else:
                print(x, "ES DEMASIADO, POSIBLEMENTE SE DESBORDE EL MAR...")
                while True:
                    xx = input("¿QUIERE CORRER EL RIESGO? SI/NO ")
                    if xx.lower() in ["si", "sí", "yes", "ja", "jaa", "n"]:
                        print("SU TABLERO DE ", x, "FILAS Y ", x, "COLUMNAS SE ESTÁ CREANDO.\n")
                        return x
                    elif xx.lower() in ["no", "n", "nein", "nope"]:
                        print("SU TABLERO SERÁ DE 25 FILAS Y 25 COLUMNAS")
                        x= 23
                        print("SU TABLERO DE ", x, "FILAS Y ", x, "COLUMNAS SE ESTÁ CREANDO.\n")
                        return x
                    else:
                        print("POR FAVOR, INGRESE 'SI' O 'NO'.")

           
def tablero(Tm):

    nosotros = np.full((Tm, Tm), "🟦")
    ordenador = np.full((Tm, Tm), "🟦")
    separador = np.full((Tm+1, 2), "🟫")  
    numeros_de_columnas = []  # Para las fila con los números que indican las columnas necesitamos crear una lista vacia
    for i in range(1, Tm + 1):  #vamos recorriendo el rango (empezando en 1, no en 0, y terminando en Tm(o sea, uno más))
        if i < 10:  
            numeros_de_columnas.append(" "+str(i))  #A los número de un digito le añado un espacio para que queden bien y no se amontonen.
        else:
            numeros_de_columnas.append(str(i))   
    nosotros_columna= np.vstack((nosotros, numeros_de_columnas))
    ordenador_columna= np.vstack((ordenador, numeros_de_columnas))
    pantallas= np.hstack((nosotros_columna, separador,ordenador_columna))
    espacio_vacio= np.array([[" "]]) #para que pueda unir matrices con distinta dimension necesito añadir espacios vacios
    columnasletras = np.array([chr((i % 26) + 65) if i < 26 else chr((i % 26) + 97) for i in range(Tm)]).reshape(-1, 1)#esta linea es bastante complicada, lo hice con gpt.
    columna_de_letras =np.vstack((columnasletras, espacio_vacio))
    columna_de_filas_vacias = np.array([[" "]]*(Tm+1)) #para que la columna de letras que indican los nombres de las filas no se amontonen (en la pantalla derecha) usamos una columna vacia.
    pantallas_con_filas = np.hstack((columna_de_letras, pantallas,columna_de_filas_vacias, columna_de_letras))
    return pantallas_con_filas


def colocador_aleatorio_barcos_jugador(tablero, Tm):
  
    barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for eslora in barcos:
        while True:
            x = random.randint(0,Tm) 
            y = random.randint(1, Tm+2)
            dirección = random.choice(direcciones)
            válido = True
            for i in range(eslora):
                nuevo_x = x + dirección[0] * i
                nuevo_y = y + dirección[1] * i
                if not (0 <= nuevo_x < Tm and 0 <= nuevo_y < Tm) or tablero[nuevo_x][nuevo_y] != "🟦":
                    válido = False
                    break
            if válido:
                for i in range(eslora):
                    tablero[x + dirección[0] * i][y + dirección[1] * i] = "⬛"
                break





def colocador_aleatorio_barcos_ordenador(tablero, Tm):
  
    barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for eslora in barcos:
        while True:
            x = random.randint(0,Tm) 
            y = random.randint(Tm+3, Tm*2+4)
            dirección = random.choice(direcciones)
            válido = True
            for i in range(eslora):
                nuevo_x = x + dirección[0] * i
                nuevo_y = y + dirección[1] * i
                if not (0 <= nuevo_x < (Tm*2+5) and 0 <= nuevo_y < (Tm*2+5)) or tablero[nuevo_x][nuevo_y] != "🟦":
                    válido = False
                    break
            if válido:
                for i in range(eslora):
                    tablero[x + dirección[0] * i][y + dirección[1] * i] = "⬜"
                break



#creo que seria que "el main" fuera de este tipo... solo los importas y las llamadas a las funciones

tamaño_tablero = selector_tamaño()

tablero_resultante = tablero(tamaño_tablero)# Llamamos a la función tablero con el tamaño seleccionado y almacenamos el resultado
colocador_aleatorio_barcos_jugador(tablero_resultante, tamaño_tablero) 
colocador_aleatorio_barcos_ordenador(tablero_resultante, tamaño_tablero) #colocamos los barcos despues de crear el tablero
# Imprimimos el tablero resultante
tabla_info_pd = marcador(yo, enemigo)






print(tabla_info_pd)
for fila in tablero_resultante:
    print("".join(fila))









