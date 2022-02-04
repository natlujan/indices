import numpy as np

data = np.arange(0, 11)
indice = -7.0

print(data)

print("Índice 0: " + str(data[0]) )
print("Índice 3: " + str(data[3]) )

# index out of bounds
# print("índice 16: " + str(data[16]) )

# si usamos variables en los índices
# tienen que ser int (número entero)
# puede ser negativo

print("Índice índice: " + str(data[int(indice)]) )

# si usamos negativos, se recorre en reversa
# comenzando desde el -1

print("Índice -1: " + str(data[-1]) )
print("Índice -7: " + str(data[-7]) )

# index out of bounds
# print("índice -11: " + str(data[-16]) )

# rangos [m:n]
# m se incluye
# n se excluye

# rango siempre regresa un arreglo

print("Índice [0:5]: " + str(data[0:5]) )

# me regresa un arreglo vacío

print("Índice [1:1]: " + str(data[1:1]) )

print("Índice [1:2]: " + str(data[1:2]) )

# si no le doy rangos válidos, me regresa vacío

print("Índice [4:1]: " + str(data[4:1]) )

# no existe el índice 11, pero no marca error
# porque nunca intenta acceder a él

print("Índice [1:11]: " + str(data[1:11]) )

# si se sale de los límites, no marca error,
# solo te regresa hasta donde puede

print("Índice [1:16]: " + str(data[1:16]) )

# estos rangos sí son válidos, aunque sean negativos,
# la n (segundo dato del rango) siempre es excluyente

print("Índice [1:-1]: " + str(data[1:-1]) )

print("Índice [1:-3]: " + str(data[1:-3]) )

# el tercer parámetro del rango es el "step"

print("Índice [1:-1]: " + str(data[1:-1:2]) )

# los parámetros de los rangos son opcionales
# si se omite el primero (m) lo toma como el primer elemento

print("Índice [:5]: " + str(data[:5]) )

# si se omite el segundo (n) lo toma como el último elemento

print("Índice [2:]: " + str(data[2:]) )

print("Índice [-6:]: " + str(data[-6:]) )

# si se omiten ambos parámetros (m y n) lo toma como
# desde el primero hasta el último
# sólo se contempla el step

print("Índice [::2]: " + str(data[::2]) )

# si los valores del step son negativos
# primero invierte el arreglo

print("Índice [::-1]: " + str(data[::-1]) )
print("Índice [::-2]: " + str(data[::-2]) )

elemento = data[5]
elemento = 7

# data[5] = 7

print("Elemento: " + str(elemento) )
print("Data: " + str(data) )

# si se modifica un segmento obtenido por rango de un ndarray
# tambien se ve modificado el ndarray original

segmento = data[1:6:2]
print("Segmento: " + str(segmento) )
segmento[0] = 24
print("Segmento modificado: " + str(segmento) )
print("Data: " + str(data) )


data[5] = 48
print("Data: " + str(data) )
print("Segmento: " + str(segmento) )

















