from utils import tablero, colocar_barcos_aleatorios, turno_juego

# Crear tableros iniciales
tablero_jugador = tablero()
tablero_rival = tablero()

print("Tablero jugador:")
print(tablero_jugador)

# Colocar los barcos
flota = [4, 3, 3, 2, 2, 2]
colocar_barcos_aleatorios(tablero_jugador, flota)

print("Tablero jugador con barcos:")
print(tablero_jugador)

# Iniciar el sistema de turnos
turno_juego()
