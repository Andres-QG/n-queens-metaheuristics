# Algoritmo genético para el problema de las n-reinas

import random

# Genera un tablero con posiciones aleatorias
def generar_tablero(tamano):
    tablero = [random.randint(0, (tamano-1)) for _ in range(tamano)]
    return tablero

