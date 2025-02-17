# 📌 Ejemplos de Tuplas en Python

import os
os.system("cls")

# 1️⃣ Creación de una tupla
mi_tupla = (1, 2, 3, 2, 2)
print("Tupla original:", mi_tupla)

# 2️⃣ Intentar modificar un valor en la tupla (esto dará error)
# mi_tupla[0] = 5  # ❌ TypeError: 'tuple' object does not support item assignment

# 3️⃣ Solución: Convertir la tupla en lista, modificarla y volver a tupla
lista = list(mi_tupla)  # Convertir a lista
lista[0] = 5  # Modificar el primer elemento
mi_tupla = tuple(lista)  # Convertir de nuevo a tupla
print("Tupla modificada convirtiéndola en lista:", mi_tupla)

# 4️⃣ Crear una nueva tupla con valores modificados
mi_tupla = (5,) + mi_tupla[1:]
print("Nueva tupla con valores modificados:", mi_tupla)

# 5️⃣ Acceder a elementos de una tupla
print("Primer elemento:", mi_tupla[0])
print("Último elemento:", mi_tupla[-1])

# 6️⃣ Longitud de una tupla con propiedad len()
print("Número de elementos en la tupla:", len(mi_tupla))

# 7️⃣ Métodos disponibles en una tupla count() e index()
print("Cantidad de veces que aparece el 2 en la tupla:", mi_tupla.count(2))
print("Índice de la primera aparición del 2 en la tupla:", mi_tupla.index(2))
