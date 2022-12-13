import random 
import numpy as np

class Tablero:
    dimensiones = (10,10)
    tablero = np.full((10,10), " ")
    tablero_disparos = np.full((10,10), " ")


    def __init__(self,id=int,barcos=dict()):
        self.id = id
        self.barcos = dict(barcos)
    
    def generar_b_aleatorio(self,eslora):
        barco_random = []
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
        orien = random.choice(["Norte", "Sur", "Este", "Oeste"])
        barco_random.append((fila_random,columna_random))
        while len(barco_random) < eslora:
            if orien == "Norte":
                fila_random = fila_random - 1
            if orien == "Sur":
                fila_random = fila_random + 1
            if orien == "Este":
                columna_random = columna_random + 1
            if orien == "Oeste":
                columna_random = columna_random - 1
            if fila_random < 0 or fila_random >= 10 or columna_random < 0 or columna_random >= 10:
                continue
            barco_random.append((fila_random,columna_random))
        
        for i in barco_random:
            if self.tablero[i] == 'O':
                continue
            else:
                self.tablero[i] = 'O'
        return barco_random

    def disparar(self):
        disparo = input('Introduce las coordenadas donde quieres disparar')
        return disparo
    
    def disparar_random(self):
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)      
        disp = (fila_random,columna_random)      
        return disp

            
            
    