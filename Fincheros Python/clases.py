#CLASES
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
                    if not (0 <= nuevo_x < 10 and 0 <= nuevo_y < 10) or self.tablero[nuevo_x][nuevo_y][0] != self.agua_c[0]:
                        válido = False
                        break
                if válido:
                    for i in range(eslora):
                        self.tablero[x + dirección[0] * i][y + dirección[1] * i] = self.barco_c #str(eslora)
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


class Jugador:
    nombre = "Jugador_0"
    alias = "Blas de Lezo"    
    
    def __init__(self, nom, ali):
        self.nombre = nom
        self.alias = ali
    
    def cambiar_alias(self,ali):
        self.alias = ali
    
    #desarrollar las funciones que hagan la introdcuccion de datos por el jugador     


class Barco:
    eslora = 0  
    nombre = "Nave_0"

    def __init__(self, nom, esl):
        self.nombre = nom
        self.eslora = esl

    def nombrar_barco(self,nom):
        self.nombre = nom

    def eslorar_barco(self, esl):
        self.eslora = esl


        