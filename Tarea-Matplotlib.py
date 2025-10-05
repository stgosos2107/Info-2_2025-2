"""Tarea Matplotlib
Santiago Osorio Salazar"""

import numpy as np
import matplotlib.pyplot as plt

# Semilla para reproducibilidad
np.random.seed(42)

# 1) Crear vector y matriz
vector = np.random.rand(720)
M = vector.reshape((120, 6))
M_T = M.T

# 2) Crear figura y subplots (2 filas x 3 columnas)
fig, axs = plt.subplots(2, 3, figsize=(14, 8))
axs = axs.ravel()

# 3) Gráficos distintos por panel

# Panel 1: Plot (línea)
axs[0].plot(M_T[0], color='tab:blue')
axs[0].set_title('Plot')
axs[0].set_xlabel('Índice')
axs[0].set_ylabel('Valor')
axs[0].grid(True, linestyle='--', alpha=0.5)

# Panel 2: Scatter (dispersión)
axs[1].scatter(np.arange(len(M_T[1])), M_T[1], c=M_T[1], cmap='viridis', s=25)
axs[1].set_title('Scatter')
axs[1].set_xlabel('Índice')
axs[1].set_ylabel('Valor')
axs[1].grid(True, linestyle='--', alpha=0.5)

# Panel 3: Errorbar (primeros 30 puntos)
y = M_T[2][:30]
x = np.arange(30)
error = np.random.rand(30) * 0.1
axs[2].errorbar(x, y, yerr=error, fmt='o', ecolor='purple', capsize=3, color='black')
axs[2].set_title('Errorbar (primeros 30)')
axs[2].set_xlabel('Índice')
axs[2].set_ylabel('Valor')
axs[2].grid(True, linestyle='--', alpha=0.5)

# Panel 4: Histograma
axs[3].hist(M_T[3], bins=15, color='gold', edgecolor='black')
axs[3].set_title('Histograma')
axs[3].set_xlabel('Valor')
axs[3].set_ylabel('Frecuencia')
axs[3].grid(True, linestyle='--', alpha=0.5)

# Panel 5: Barras (suma por fila)
suma = M.sum(axis=1)
axs[4].bar(np.arange(len(suma))[:10], suma[:10], color='teal', edgecolor='black')
axs[4].set_title('Bar (suma por fila)')
axs[4].set_xlabel('Índice')
axs[4].set_ylabel('Suma')
axs[4].grid(True, axis='y', linestyle='--', alpha=0.5)

# Panel 6: Pie
valores = M_T[4][:6]
porcentajes = valores / valores.sum()
labels = [f'G{i+1}' for i in range(6)]
axs[5].pie(porcentajes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[5].set_title('Pie (fila 4)')
axs[5].axis('equal')

# Ajustes finales
fig.suptitle('6 paneles con diferentes gráficos', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
