# Algoritmo genético para el problema de las n-reinas

import random

# Genera un tablero con posiciones aleatorias
def generar_tablero(tamano):
    tablero = [random.randint(0, (tamano-1)) for _ in range(tamano)]
    return tablero

# Valor preliminar
GENERACIONES_MAXIMAS = 150

# Función para calcular el fitness de un tablero, es decir comprobar si se da alguna colisión entre las reinas
def fitness(tablero):
    n = len(tablero)
    colisiones = 0
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j]:
                ataques += 1
            if abs(tablero[i] - tablero[j]) == abs(i - j):
                ataques += 1
    return colisiones

def algoritmo_genetico():
    # Se crea la población de 30 tableros para cada tratamiento
    # Tamano de tablero fijo en 8, falta hacer para que cambie a 20
    poblacion_tableros = [(generar_tablero(8), 0) for _ in range(30)]

    for generation in range(GENERACIONES_MAXIMAS):
        poblacion_tableros = [(tablero, fitness(tablero)) for tablero, _ in poblacion_tableros]
