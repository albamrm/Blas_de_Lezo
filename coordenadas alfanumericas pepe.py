Tm =20

coordenadas_jugador = []
letra_a_numero = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
#1 barco 1 posicion
while True:
    b1_1 = input("INGRESE LAS COORDENADAS PARA SU PRIMER BARCO DE UNA POSICION. (ejemplo: A9) ")
    if len(b1_1) > 3: #con esto nos aseguramos que no se metan valores locos
        print("POR FAVOR INGRESE LOS VALORES ADECUADAMENTE.")
        continue
    letra = b1_1[0]
    if letra.lower() not in letra_a_numero: #asi no discrimina de minisculas y mayusculas
        print("POR FAVOR INGRESE UN VALOR VÁLIDA (ejemplo: G10).")
        continue
    numero_fila = letra_a_numero[letra.lower()]
    if numero_fila > Tm:
        print("NO HAY TANTAS FILAS")
        continue
    if not b1_1[1:].isdigit():
        print("POR FAVOR INGRESE UNA COLUMNA VALIDA. (La columna es numérica)")
        continue
    numero_columna = int(b1_1[1:])
    if numero_columna > Tm:
        print("NO HAY TANTAS COLUMNAS")
        continue         
    coor_b1_1 = (numero_fila, numero_columna)
    coordenadas_jugador.append(coor_b1_1)
    break
#2 barco 1 posicion
while True:
    b1_2 = input("INGRESE LAS COORDENADAS PARA SU SEGUNDO BARCO DE UNA POSICION. (ejemplo: K10) ")
    if len(b1_2) > 3: #con esto nos aseguramos que no se metan valores locos
        print("POR FAVOR INGRESE LOS VALORES ADECUADAMENTE.")
        continue
    letra = b1_2[0]
    if letra.lower() not in letra_a_numero: #asi no discrimina de minisculas y mayusculas
        print("POR FAVOR INGRESE UN VALOR VÁLIDA (ejemplo: G10).")
        continue
    numero_fila = letra_a_numero[letra.lower()]
    if numero_fila > Tm:
        print("NO HAY TANTAS FILAS")
        continue
    if not b1_2[1:].isdigit():
        print("POR FAVOR INGRESE UNA COLUMNA VALIDA. (La columna es numérica)")
        continue
    numero_columna = int(b1_2[1:])
    if numero_columna > Tm:
        print("NO HAY TANTAS COLUMNAS")
        continue
    coor_b1_2 = (numero_fila, numero_columna)
    if coor_b1_2 in coordenadas_jugador:
        print("COORDENADA OCUPADA. POR FAVOR INGRESE OTRA.")
        continue
    coordenadas_jugador.append(coor_b1_2)
    break
#3 barco 1 posicion
while True:
    b1_3 = input("INGRESE LAS COORDENADAS PARA SU TERCER BARCO DE UNA POSICION. (ejemplo: D12) ")
    if len(b1_3) > 3: #con esto nos aseguramos que no se metan valores locos
        print("POR FAVOR INGRESE LOS VALORES ADECUADAMENTE.")
        continue
    letra = b1_3[0]
    if letra.lower() not in letra_a_numero: #asi no discrimina de minisculas y mayusculas
        print("POR FAVOR INGRESE UN VALOR VÁLIDA (ejemplo: E11).")
        continue
    numero_fila = letra_a_numero[letra.lower()]
    if numero_fila > Tm:
        print("NO HAY TANTAS FILAS")
        continue
    if not b1_3[1:].isdigit():
        print("POR FAVOR INGRESE UNA COLUMNA VALIDA. (La columna es numérica)")
        continue
    numero_columna = int(b1_3[1:])
    if numero_columna > Tm:
        print("NO HAY TANTAS COLUMNAS")
        continue
    coor_b1_3 = (numero_fila, numero_columna)
    if coor_b1_3 in coordenadas_jugador:
        print("COORDENADA OCUPADA. POR FAVOR INGRESE OTRA.")
        continue
    coordenadas_jugador.append(coor_b1_3)
    break 
#4 barco 1 posicion

while True:
    b1_4 = input("INGRESE LAS COORDENADAS PARA SU ÚLTIMO BARCO DE UNA POSICION. (ejemplo: D12) ")
    if len(b1_4) > 3: #con esto nos aseguramos que no se metan valores locos
        print("POR FAVOR INGRESE LOS VALORES ADECUADAMENTE.")
        continue
    letra = b1_4[0]
    if letra.lower() not in letra_a_numero: #asi no discrimina de minisculas y mayusculas
        print("POR FAVOR INGRESE UN VALOR VÁLIDA (ejemplo: E11).")
        continue
    numero_fila = letra_a_numero[letra.lower()]
    if numero_fila > Tm:
        print("NO HAY TANTAS FILAS")
        continue
    if not b1_4[1:].isdigit():
        print("POR FAVOR INGRESE UNA COLUMNA VALIDA. (La columna es numérica)")
        continue
    numero_columna = int(b1_4[1:])
    if numero_columna > Tm:
        print("NO HAY TANTAS COLUMNAS")
        continue
    coor_b1_4 = (numero_fila, numero_columna)
    if coor_b1_4 in coordenadas_jugador:
        print("COORDENADA OCUPADA. POR FAVOR INGRESE OTRA.")
        continue
    coordenadas_jugador.append(coor_b1_4)
    break

#bARCOS DE  2 posiciones 
numero_de_barco_de_dos = 1
barcos_dos= []
while len(barcos_dos) < 3: 
    dirc= input(f'¿QUE DIRECCION TENDRÁ SU BARCO DE 2 POSICIONES NÚMERO {numero_de_barco_de_dos}? V para vertical H PARA horizontal ')  
    if dirc.lower() not in ("h", "v", " h", " v"," h ", " v "):
        continue 
    else: 
        if dirc.lower() in ("h"," h"," h "):
            direccion_b2_1 = 2
        else:
            direccion_b2_1= 1
    #ELEGIMOS COORDENADAS DE POPA
    b2_1 = input(F"INGRESE LA COORDENADA PARA LA POPA DE SU BARCO DE 2 POSICIONES NÚMERO {numero_de_barco_de_dos}(ejemplo: K10) ")
    if len(b2_1) > 3: #con esto nos aseguramos que no se metan valores locos
        print("POR FAVOR INGRESE LOS VALORES ADECUADAMENTE.")
        continue
    letra = b2_1[0]
    if letra.lower() not in letra_a_numero: #asi no discrimina de minisculas y mayusculas
        print("POR FAVOR INGRESE UN VALOR VÁLIDA (ejemplo: G10).")
        continue
    numero_fila = letra_a_numero[letra.lower()]
    if numero_fila > Tm:
        print("NO HAY TANTAS FILAS, VUELVA A ELEGIR DIRECCIÓN Y COORDENADA DE LA POPA")
        continue      
    if not b2_1[1:].isdigit():
        print("POR FAVOR INGRESE UNA COLUMNA VALIDA. (La columna es numérica)")
        continue
    numero_columna = int(b2_1[1:])
    if numero_columna > Tm:
        print("NO HAY TANTAS COLUMNAS")
        continue
    coor_b1_1 = (numero_fila, numero_columna)
    if coor_b1_1 in coordenadas_jugador:
        print("COORDENADA OCUPADA. POR FAVOR INGRESE OTRA.")
        continue
    popa_b2_1 = (coor_b1_1)
    if direccion_b2_1 == 1:  # Barco en vertical
        if numero_fila + 1 < Tm and (numero_fila + 1, numero_columna) not in coordenadas_jugador:
            proa_b2_1 = (numero_columna + 1, numero_columna)
        else:
            print("EL BARCO NO CABE AHÍ, ELIJA OTRAS COORDENADAS")
            continue      
    else:  # Barco en horizontal
        if numero_columna + 1 < Tm and (numero_fila, numero_columna + 1) not in coordenadas_jugador:
            proa_b2_1 = (numero_fila, numero_columna + 1)
        else:
            print("EL BARCO NO CABE AHÍ, ELIJA OTRAS COORDENADAS")
            continue
    if popa_b2_1 in coordenadas_jugador or proa_b2_1 in coordenadas_jugador:
        print("EL BARCO NO CABE AHÍ, ELIJA OTRAS COORDENADAS")
        continue
    coordenadas_jugador.append(proa_b2_1)
    coordenadas_jugador.append(popa_b2_1)
    barcos_dos.append(proa_b2_1)#esto es para que se corra 3 veces
    numero_de_barco_de_dos = numero_de_barco_de_dos +1
   
 


    
   


print(coordenadas_jugador)