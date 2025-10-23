import numpy as np
import random

# CREAR TABLERO VACÍO

def tablero():
    # Crea una matriz 10x10 llena con el carácter "~"
    return np.full((10, 10), "-")

# COLOCAR BARCOS

def colocar_barcos(tablero, lista_posiciones):
    for fila, col in lista_posiciones:
        tablero[fila, col] = "O"  
    return tablero

# COLOCAR BARCOS ALEATORIOS
# ========================
def colocar_barcos_aleatorios(tablero, tamaños_barcos):
    for tamaño in tamaños_barcos:
        colocado = False
        while not colocado:
            orientacion = random.choice(["H", "V"])
            fila = random.randint(0, 9)
            col = random.randint(0, 9)

            if orientacion == "H":
                # Verifica que quepa y no haya solapamiento
                if col + tamaño <= 10 and np.all(tablero[fila, col:col+tamaño] == "-"):
                    tablero[fila, col:col+tamaño] = "O"
                    colocado = True
            else:  # Vertical
                if fila + tamaño <= 10 and np.all(tablero[fila:fila+tamaño, col] == "-"):
                    tablero[fila:fila+tamaño, col] = "O"
                    colocado = True
    return tablero
# DISPARAR

def disparar(tablero, fila, col):
    if tablero[fila, col] == "O":
        tablero[fila, col] = "X"
        print("Tocado")
        return True
    elif tablero[fila, col] == "-":
        tablero[fila, col] = "A"
        print("Agua.")
        return False
    else:
        print("Ya disparaste ahí.")
        return False


# VERIFICAR SI QUEDAN BARCOS

def tablero_vacio(tablero):
    return not np.any(tablero == "O")

# TURNOS

def turno_juego():
    # Crear tableros vacíos
    tablero_j1 = tablero()
    tablero_j2 = tablero()

    # Colocar barcos de forma aleatoria
    flota = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    colocar_barcos_aleatorios(tablero_j1, flota)
    colocar_barcos_aleatorios(tablero_j2, flota)

    turno = 1  # Empieza el jugador humano

    while True:
        print(f"Turno del Jugador {turno}")

        if turno == 1:
            print("Tu tablero:")
            print(tablero_j1)
            print("Tablero rival:")
            print(tablero_j2)

            fila = int(input("Fila (0-9): "))
            col = int(input("Columna (0-9): "))

            acierto = disparar(tablero_j2, fila, col)
            if tablero_vacio(tablero_j2):
                print("¡Has ganado!")
                break
            turno = 2

        else:
            # Turno de la máquina (IA simple)
            fila = random.randint(0, 9)
            col = random.randint(0, 9)
            print(f"La máquina dispara en ({fila}, {col})")

            acierto = disparar(tablero_j1, fila, col)
            if tablero_vacio(tablero_j1):
                print("La máquina ha ganado")
                break
            turno = 1