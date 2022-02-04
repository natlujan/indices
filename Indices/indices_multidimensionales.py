import numpy as np

data = np.array([ [ 0,  1,  2,  3,  4,  5],
                  [10, 11, 12, 13, 14, 15],
                  [20, 21, 22, 23, 24, 25],
                  [30, 31, 32, 33, 34, 35],
                  [40, 41, 42, 43, 44, 45],
                  [50, 51, 52, 53, 54, 55] ]) 

print(str(data) )

# matrices los índices son [fila, columna]

print("Índice [4, 4]:" + str(data[4, 4]) )

# extraer una columna

print("Índice [:, 1]:" + str(data[:, 1]) )

# extraer una fila

print("Índice [3, :]:" + str(data[3, :]) )


