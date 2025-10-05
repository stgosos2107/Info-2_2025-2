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