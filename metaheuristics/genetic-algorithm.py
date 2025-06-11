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

def seleccion(poblacion, cantidad_muestra):
    tableros_seleccionados = []
    for _ in range(len(poblacion)):
        muestra = random.sample(poblacion, cantidad_muestra)
        mejores = min(muestra, key=lambda x: x[1])
        tableros_seleccionados.append(mejores)
    return tableros_seleccionados

def cruce(primer_padre, segundo_padre):
    print("En proceso...")

def mutacion(tablero, tasa_mutacion):
    print("En proceso...")

# Implementación del algoritmo genético
def algoritmo_genetico():
    # Las 30 réplicas
    for replica in range(30):
        inicio = time.time()

        # Se crea la población de 50 tableros para cada tratamiento
        # Tamano de tablero fijo en 8, falta hacer para que cambie a 20
        poblacion_tableros = [(generar_tablero(8), 0) for _ in range(TAMANO_POBLACION)]
        generation = 0
        solucion_optima = False
        while generation < GENERACIONES_MAXIMAS and solucion_optima == False:
            generation = generation + 1
            poblacion_tableros = [(tablero, fitness(tablero)) for tablero, _ in poblacion_tableros]

            mejor_tablero, mejor_fitness = min(poblacion_tableros, key=lambda x: x[1])
            # print("Mejor tablero:", mejor_tablero)
            # print("Mejor fitness:", mejor_fitness)

            next_generation = []

            if mejor_fitness == 0:
                print("Mejor tablero:", mejor_tablero)
                print("Mejor fitness:", mejor_fitness)
                solucion_optima_encontrada = True
            else:
                pool_padres = seleccion(poblacion_tableros, 4)

                while len(next_generation) < len(poblacion_tableros):

                    # Selección de padres para posterior cruce, se usa '[0]' ya que al ser una tupla con el tablero y 
                    # el fitness, solo necesitamos el tablero para crear la nueva población
                    primer_padre = random.choice(pool_padres)[0]
                    segundo_padre = random.choice(pool_padres)[0]
                    # print("Padre 1:", primer_padre)
                    # print("Padre 2:", segundo_padre)

                    # TODO: Incluir métodos de algoritmos genéticos de cruce y mutación
                    # TODO: Definir tasa de mutación
                    next_generation = poblacion_tableros
                    poblacion_tableros = next_generation

        fin = time.time()
        print(f"Réplica: {replica + 1} | Tiempo = {fin - inicio:.4f} segundos | Iteraciones: {generation}")

if __name__ == "__main__":
    algoritmo_genetico()