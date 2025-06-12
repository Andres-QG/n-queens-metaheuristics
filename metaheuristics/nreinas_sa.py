import random
import math
import time
import psutil
import csv

def calcular_conflictos(tablero):
    n = len(tablero)
    conflictos = 0
    for i in range(n):
        for j in range(i+1, n):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j):
                conflictos += 1
    return conflictos

def vecino(tablero):
    n = len(tablero)
    nuevo_tablero = tablero[:]
    fila = random.randint(0, n-1)
    nueva_col = random.randint(0, n-1)
    while nueva_col == nuevo_tablero[fila]:
        nueva_col = random.randint(0, n-1)
    nuevo_tablero[fila] = nueva_col
    return nuevo_tablero

def simulated_annealing(n, t_inicial=1.0, t_final=1e-6, alpha=0.9995, max_iter=20000):
    estado = [random.randint(0, n-1) for _ in range(n)]
    t = t_inicial
    iteracion = 0

    while t > t_final and iteracion < max_iter:
        costo_actual = calcular_conflictos(estado)
        if costo_actual == 0:
            return estado, iteracion
        vecino_estado = vecino(estado)
        costo_vecino = calcular_conflictos(vecino_estado)
        delta = costo_vecino - costo_actual
        if delta < 0 or random.random() < math.exp(-delta / t):
            estado = vecino_estado
        t *= alpha
        iteracion += 1
    return None, iteracion

def correr_experimento(N, repeticiones=30, writer=None):
    print(f"\n=== Experimento para N={N} ===")
    exitos = 0
    for i in range(repeticiones):
        cpu_inicio = psutil.cpu_percent(interval=None)
        memoria_inicio = psutil.virtual_memory().available / (1024 * 1024)

        start = time.time()
        solucion, iters = simulated_annealing(N)
        end = time.time()

        cpu_fin = psutil.cpu_percent(interval=None)
        memoria_fin = psutil.virtual_memory().available / (1024 * 1024)
        tiempo = end - start

        exito = solucion is not None
        if exito:
            exitos += 1

        print(f"Corrida {i+1}: {'Exito' if exito else 'Fracaso'} | "
              f"Tiempo = {tiempo:.4f} s | Iteraciones: {iters} | "
              f"CPU inicio: {cpu_inicio:.1f}%, CPU fin: {cpu_fin:.1f}% | "
              f"Memoria inicio: {memoria_inicio:.2f} MB, fin: {memoria_fin:.2f} MB")

        if writer:
            writer.writerow({
                "N": N,
                "Corrida": i + 1,
                "Exito": int(exito),
                "Tiempo_s": round(tiempo, 6),
                "Iteraciones": iters,
                "CPU_inicio_%": round(cpu_inicio, 1),
                "CPU_fin_%": round(cpu_fin, 1),
                "Memoria_inicio_MB": round(memoria_inicio, 2),
                "Memoria_fin_MB": round(memoria_fin, 2)
            })

    print(f"\nTotal exitos: {exitos} de {repeticiones}\n")

if __name__ == "__main__":
    with open("datos.csv", "w", newline="") as csvfile:
        fieldnames = [
            "N", "Corrida", "Exito", "Tiempo_s", "Iteraciones",
            "CPU_inicio_%", "CPU_fin_%", "Memoria_inicio_MB", "Memoria_fin_MB"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for N in [8, 20]:
            correr_experimento(N, repeticiones=30, writer=writer)
