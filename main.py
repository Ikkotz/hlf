from utils import tablero, colocar_barcos_aleatorios, turno_juego

# Crear tableros iniciales
tablero_jugador = tablero()
tablero_rival = tablero()

# Colocar los barcos
flota = [4, 3, 3, 2, 2, 2]
colocar_barcos_aleatorios(tablero_jugador, flota)
# Iniciar el sistema de turnos
turno_juego()
