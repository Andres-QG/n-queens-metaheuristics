# Algoritmo genético para el problema de las n-reinas

import random
import time

# Genera un tablero con posiciones aleatorias
def generar_tablero(tamano):
    tablero = [random.randint(0, (tamano-1)) for _ in range(tamano)]
    # print("tablero: ", tablero)
    return tablero

# Valor preliminar
GENERACIONES_MAXIMAS = 150
TAMANO_POBLACION = 50

# Función para calcular el fitness de un tablero, es decir comprobar si se da alguna colisión entre las reinas
def fitness(tablero):
    n = len(tablero)
    colisiones = 0
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j]:
                colisiones += 1
            if abs(tablero[i] - tablero[j]) == abs(i - j):
                colisiones += 1
    return colisiones

# Implementación del algoritmo genético
def algoritmo_genetico():
    # Las 30 réplicas
    for replica in range(30):
        inicio = time.time()

        # Se crea la población de 50 tableros para cada tratamiento
        # Tamano de tablero fijo en 8, falta hacer para que cambie a 20
        poblacion_tableros = [(generar_tablero(8), 0) for _ in range(TAMANO_POBLACION)]

        for generation in range(GENERACIONES_MAXIMAS):
            poblacion_tableros = [(tablero, fitness(tablero)) for tablero, _ in poblacion_tableros]

        mejor_tablero, mejor_fitness = min(poblacion_tableros, key=lambda x: x[1])
        print("Mejor tablero:", mejor_tablero)
        print("Mejor fitness:", mejor_fitness)

        next_generation = []

        if mejor_fitness == 0:
            print("Mejor tablero:", mejor_tablero)
            print("Mejor fitness:", mejor_fitness)
        else:
            # while len(next_generation) < len(poblacion_tableros):
            #     print("hola")
                # TODO: Incluir métodos de algoritmos genéticos selección, cruce y mutación
                # TODO: Definir tasa de mutación

            

        fin = time.time()
        print(f"Réplica: {replica + 1} | Tiempo = {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    algoritmo_genetico()