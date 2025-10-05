"""Tarea Matplotlib
Santiago Osorio Salazar"""

import numpy as np
import matplotlib.pyplot as plt

# Semilla para reproducibilidad
np.random.seed(42)

# 1) Crear un vector de tamaño 720 con valores aleatorios
vector = np.random.rand(720)

# 2) Cambiar su forma a una matriz de 120 filas y 6 columnas
M = vector.reshape((120, 6))

# 3) Crear la transpuesta y copias con diferentes órdenes de memoria
M_T = M.T
M_C = M_T.copy(order='C')
M_F = M_T.copy(order='F')

print(f"Shapes -> M: {M.shape}, M_T: {M_T.shape}")
print("M_T contiguo C?:", M_T.flags['C_CONTIGUOUS'], " / F?:", M_T.flags['F_CONTIGUOUS'])
print("M_C contiguo C?:", M_C.flags['C_CONTIGUOUS'], " / F?:", M_C.flags['F_CONTIGUOUS'])
print("M_F contiguo C?:", M_F.flags['C_CONTIGUOUS'], " / F?:", M_F.flags['F_CONTIGUOUS'])

# 4) Crear figura con 6 subgráficos “a mano”
fig = plt.figure(figsize=(16, 10))
rects = [
    [0.05, 0.68, 0.58, 0.27],
    [0.67, 0.68, 0.28, 0.27],
    [0.05, 0.38, 0.42, 0.23],
    [0.50, 0.38, 0.45, 0.23],
    [0.05, 0.05, 0.42, 0.25],
    [0.52, 0.03, 0.23, 0.30],
]
axs = [fig.add_axes(r) for r in rects]

# 5) Asignar cada fila de la transpuesta a un gráfico distinto
r0, r1, r2, r3, r4, r5 = M_T