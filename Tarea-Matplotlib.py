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

# Panel 1: gráfico de línea
axs[0].plot(r0, label='Fila 0 (línea)')
axs[0].set_title('Línea – Fila 0')
axs[0].set_xlabel('Índice')
axs[0].set_ylabel('Valor')
axs[0].legend()
axs[0].grid(True, linestyle='--', alpha=0.5)

# Panel 2: gráfico de dispersión
axs[1].scatter(np.arange(r1.size), r1, s=16, label='Fila 1 (scatter)')
axs[1].set_title('Dispersión – Fila 1')
axs[1].set_xlabel('Índice')
axs[1].set_ylabel('Valor')
axs[1].legend()
axs[1].grid(True, linestyle=':', alpha=0.5)

# Panel 3: gráfico de barras
idx20 = np.arange(20)
axs[2].bar(idx20, r2[:20], label='Fila 2 (barras)')
axs[2].set_title('Barras – Fila 2 (20 primeros)')
axs[2].set_xlabel('Índice')
axs[2].set_ylabel('Valor')
axs[2].legend()
axs[2].grid(True, axis='y', linestyle='--', alpha=0.5)

# Panel 4: histograma
axs[3].hist(r3, bins=20, label='Fila 3 (histograma)', alpha=0.85)
axs[3].set_title('Histograma – Fila 3')
axs[3].set_xlabel('Valor')
axs[3].set_ylabel('Frecuencia')
axs[3].legend()
axs[3].grid(True, linestyle='--', alpha=0.5)