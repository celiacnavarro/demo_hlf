import numpy as np
import random

def inicializar_tablero(tamaño=10):
    tablero_usuario = np.full((tamaño,tamaño), " ")
    return tablero_usuario

def barcos_1(tablero_usuario):
  print("Para comenzar, debes colocar 4 barcos de 1 posición de eslora")
  for i in range(4):
    print("Barco:", i+1)
    a = input()
    [x,y] = a.split(',')
    [x,y] = [int(x), int(y)]
      # Validamos que las coordenadas ingresadas sean válidas y no estén ocupadas
    if x >= 0 and x < 10 and y >= 0 and y < 10 and tablero_usuario[x][y] != "O":
    # Colocamos el barco en el tablero
      tablero_usuario[x][y] = "O"
    else:
     print("Coordenadas inválidas. Intente nuevamente.")
    
def barcos_2(tablero_usuario):
  print("Ahora debes colocar 3 barcos de 2 posiciones de eslora")
  for i in range(3):
    print('Barco:', i+1)
    for i in range(2):
      a = input()
      [x,y] = a.split(',')
      [x,y] = [int(x), int(y)]
      if x >= 0 and x < 10 and y >= 0 and y < 10 and tablero_usuario[x][y] != "O":
        tablero_usuario[x][y] = "O"
      else:
        print("Coordenadas inválidas. Intente nuevamente.")
        continue


def barcos_3(tablero_usuario):
  print("Ahora debes colocar 2 barcos de 3 posiciones de eslora")
  for i in range(2):
    print('Barco:', i+1)
    for i in range(3):
      a = input()
      [x,y] = a.split(',')
      [x,y] = [int(x), int(y)]
      if x >= 0 and x < 10 and y >= 0 and y < 10 and tablero_usuario[x][y] != "O":
        tablero_usuario[x][y] = "O"
      else:
        print("Coordenadas inválidas. Intente nuevamente.")
        continue


def barcos_4(tablero_usuario):
  print("Por último, debes colocar un barco de 4 posiciones de eslora")
  for i in range(4):
    a = input()
    [x,y] = a.split(',')
    [x,y] = [int(x), int(y)]
    if x >= 0 and x < 10 and y >= 0 and y < 10 and tablero_usuario[x][y] != "O":
      tablero_usuario[x][y] = "O"
    else:
      print("Coordenadas inválidas. Intente nuevamente.")
      continue


def generar_b_aleatorio(eslora):
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

        barco_random.append((fila_random,columna_random))
        return barco_random

    