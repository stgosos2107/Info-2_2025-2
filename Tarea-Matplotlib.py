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

# Ajuste automático de márgenes y espaciado
fig.subplots_adjust(top=0.90, bottom=0.08, hspace=0.5, wspace=0.4)

# Título general ajustado (más bajo y centrado)
fig.suptitle('Ejercicio NumPy + Matplotlib (subplots a mano)',
             fontsize=16, y=0.97, fontweight='bold')


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

# Panel 5: boxplot
axs[4].boxplot(r4, vert=True, widths=0.5)
axs[4].set_title('Caja y Bigotes – Fila 4')
axs[4].set_ylabel('Valor')
axs[4].grid(True, axis='y', linestyle='--', alpha=0.5)
axs[4].plot([], [], label='Fila 4')
axs[4].legend(loc='upper right')

# Panel 6: gráfico de pastel
sizes = r5[:6]
sizes = sizes / sizes.sum()
labels = [f'S{i}' for i in range(1, 7)]
axs[5].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[5].set_title('Pastel – Fila 5 (primeros 6)')
axs[5].axis('equal')
axs[5].legend(labels, loc='lower center', bbox_to_anchor=(0.5, -0.08), ncol=3, frameon=False)

# Ajuste automático y título general
fig.subplots_adjust(top=0.90, bottom=0.08, hspace=0.5, wspace=0.4)
fig.suptitle('Ejercicio NumPy + Matplotlib (subplots a mano)',
             fontsize=16, y=0.97, fontweight='bold')

plt.show()
