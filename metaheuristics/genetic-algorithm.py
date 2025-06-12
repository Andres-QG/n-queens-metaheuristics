# Algoritmo genético para el problema de las n-reinas
import random
import time


# Genera un tablero con posiciones aleatorias
def generar_tablero(tamano):
    tablero = list(range(tamano))
    random.shuffle(tablero)
    return tablero

# Función para calcular el fitness de un tablero,
# es decir, comprobar si se da alguna colisión entre las reinas
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
    n = len(primer_padre)
    a, b = sorted(random.sample(range(n), 2))
    intermedio = primer_padre[a:b]
    resto = [gen for gen in segundo_padre if gen not in intermedio]
    hijo = resto[:a] + intermedio + resto[a:]
    return hijo


def mutacion(tablero):
    pos1, pos2 = random.sample(range(len(tablero)), 2)
    tablero[pos1], tablero[pos2] = tablero[pos2], tablero[pos1]
    return tablero

def algoritmo_genetico(Tamano):
    print(f"=== Experimento para N={Tamano} ===")

    tasa_mutacion = 0.05 if Tamano <= 8 else 0.01
    GENERACIONES_MAXIMAS = 1000 if Tamano == 8 else 50000
    TAMANO_POBLACION = 50 if Tamano <= 8 else 300

    for replica in range(30):
        inicio = time.time()
        poblacion = [(generar_tablero(Tamano), 0) for _ in range(TAMANO_POBLACION)]
        solucion_optima = False
        generacion = 0

        while generacion < GENERACIONES_MAXIMAS and not solucion_optima:
            generacion += 1
            poblacion = [(tab, fitness(tab)) for tab, _ in poblacion]
            poblacion.sort(key=lambda x: x[1])
            mejor = poblacion[0]

            if mejor[1] == 0:
                print("Mejor tablero:", mejor[0])
                print("Fitness:", mejor[1])
                solucion_optima = True
                break

            nueva_generacion = [mejor]  # elitismo: conservar el mejor

            padres = seleccion(poblacion, 5)

            while len(nueva_generacion) < TAMANO_POBLACION:
                p1 = random.choice(padres[:3])[0]  # de los mejores 3
                p2 = random.choice(padres[:3])[0]
                hijo = cruce(p1, p2)
                if random.random() < tasa_mutacion:
                    hijo = mutacion(hijo)
                nueva_generacion.append((hijo, 0))

            poblacion = nueva_generacion

        fin = time.time()
        print(f"Corrida {replica + 1} | Tiempo = {fin - inicio:.4f} s | Iteraciones: {generacion} | Mejor fitness: {mejor[1]}")

if __name__ == "__main__":
    algoritmo_genetico(8)
    algoritmo_genetico(20)