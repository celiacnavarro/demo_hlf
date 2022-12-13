import numpy as np
import random
from functions import (inicializar_tablero,barcos_1,barcos_2,barcos_3,barcos_4)
from classes import Tablero

print("Bienvenido al juego de Hundir la flota. \nEn este juego, tu rival es la máquina. \nPara comenzar, deberás colocar tus barcos en el tablero en las posiciones que prefieras.")

tablero_usuario = inicializar_tablero()
print(tablero_usuario)

barcos_1(tablero_usuario)
print(tablero_usuario)

barcos_2(tablero_usuario)
print(tablero_usuario)

barcos_3(tablero_usuario)
print(tablero_usuario)

barcos_4(tablero_usuario)
print('Así ha quedado el tablero con el que vas a jugar:')
print(tablero_usuario)

Jugador = Tablero(id=1)
Maquina = Tablero(id=0)
for i in range(4):
    Maquina.barcos['barco1', i] = Maquina.generar_b_aleatorio(1)
for i in range(3):
    Maquina.barcos['barco2', i] = Maquina.generar_b_aleatorio(2)
for i in range(2):
    Maquina.barcos['barco3', i] = Maquina.generar_b_aleatorio(3)
Maquina.barcos['barco4'] = Maquina.generar_b_aleatorio(1)

tablero_maquina = Maquina.tablero

print('Cuando sea tu turno debes introducir las coordenadas en las que quieras disparar en el tablero del rival.\nPuedes utilizar el comando "Exit" para salir del juego y "Tablero" para imprimir tu propio tablero')
modo = input('¿Te gustaría jugar en modo Fácil o Difícil? Escribe F o D')

while True:
    print('Es tu turno')
    disparo = Jugador.disparar()
    if disparo == 'Exit':
        break
    if disparo == 'Tablero':
        print(tablero_usuario)
    else:
        [x,y] = disparo.split(',')
        disparo = (int(x), int(y))
        if tablero_maquina[disparo] == 'O':
            print("Barco tocado")
            tablero_maquina[disparo] = 'X'
            Jugador.tablero_disparos[disparo] = 'X'
            if 'O' not in tablero_maquina:
                print('¡Has ganado!')
            continue
        elif tablero_maquina[disparo] == ' ':
            print("Agua")
            tablero_maquina[disparo] = '-'
            Jugador.tablero_disparos[disparo] = '-'
            print('Es el turno de la máquina')
            Maquina.disparar_random()
            print('La máquina te ha disparado en las posiciones:', disp)
            if tablero_usuario[disp] == 'O':
                print("Barco tocado")
                tablero_usuario[disp] = 'X'
                if modo == 'D':
                    orien = random.choice(["Norte", "Sur", "Este", "Oeste"])
                    if orien == 'Norte':
                        disp = disp - [1,0]
                    if orien == 'Sur':
                        disp = disp + [1,0]
                    if orien == 'Este':
                        disp = disp + [0,1]
                    if orien == 'Oeste':
                        disp = disp - [0,1]
                    while tablero_usuario[disp] == 'O':
                        print('Barco tocado')
                        if orien == 'Norte':
                            disp = disp - [1,0]
                        if orien == 'Sur':
                            disp = disp + [1,0]
                        if orien == 'Este':
                            disp = disp + [0,1]
                        if orien == 'Oeste':
                            disp = disp - [0,1]
                if 'O' not in tablero_usuario:
                    print('Has perdido')
            elif tablero_usuario[disp] == ' ':
                print("Agua")
                tablero_usuario[disp] = '-'
                print(tablero_usuario)
        print(Jugador.tablero_disparos)

        

