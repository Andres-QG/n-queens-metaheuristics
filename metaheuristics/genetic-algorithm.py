# Algoritmo genético para el problema de las n-reinas

import random

# Genera un tablero con posiciones aleatorias
def generar_tablero(tamano):
    tablero = [random.randint(0, (tamano-1)) for _ in range(tamano)]
    return tablero

# Valor preliminar
GENERACIONES_MAXIMAS = 150

def algoritmo_genetico():
    # Se crea la población de 30 tableros para cada tratamiento
    # Tamano de tablero fijo en 8, falta hacer para que cambie a 20
    poblacion_tablero = [(generar_tablero(8), 0) for _ in range(30)]

    for generation in range(GENERACIONES_MAXIMAS):
