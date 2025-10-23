Hundir la Flota (Battleship) — Python

Un sencillo juego de Hundir la Flota (Battleship) hecho en Python, jugable por consola.
El jugador compite contra una IA básica que dispara aleatoriamente.

Estructura del proyecto
hundir_la_flota

main.py          # Archivo principal — inicia el juego
utils.py         # Funciones auxiliares: tablero, barcos, disparos, etc.
README.md        # Este archivo

Requisitos

El juego usa NumPy para manejar los tableros como matrices.

Instálalo con:

pip install numpy

Cómo jugar

Ejecuta el juego desde tu terminal:

python main.py

Objetivo

Hundir todos los barcos del rival antes de que él hunda los tuyos.

Mecánica

Se crean dos tableros 10x10: uno para el jugador y otro para el rival.

Cada tablero se rellena inicialmente con "-" (agua).

Se colocan barcos automáticamente:

1 barco de tamaño 4

2 barcos de tamaño 3

3 barcos de tamaño 2

4 barcos de tamaño 1

En tu turno, introduces las coordenadas:

Fila (0-9):
Columna (0-9):


El juego indica si fue Tocado o Agua.

El primer jugador en hundir todos los barcos enemigos gana.

Símbolos del tablero
Símbolo	Significado
-	Agua
O	Parte de un barco
X	Barco tocado
A	Agua donde ya se disparó

Archivos principales
utils.py

Contiene las funciones esenciales del juego:

tablero(): Crea un tablero vacío de 10x10.

colocar_barcos_aleatorios(): Coloca los barcos de forma aleatoria sin solaparlos.

disparar(): Ejecuta un disparo y devuelve el resultado.

tablero_vacio(): Comprueba si quedan barcos en el tablero.

turno_juego(): Gestiona los turnos entre jugador y máquina.

main.py

Archivo principal del programa:

Crea los tableros iniciales.

Coloca los barcos.

Muestra los tableros.

Llama a turno_juego() para iniciar la partida.
