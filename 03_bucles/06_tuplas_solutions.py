# 📌 Soluciones a los ejercicios sobre Tuplas

# 1️⃣ Crea una tupla con los nombres de 5 ciudades y muestra la segunda y la penúltima ciudad.
ciudades = ("Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao")
print("Segunda ciudad:", ciudades[1])
print("Penúltima ciudad:", ciudades[-2])

# 2️⃣ Dada una tupla con números enteros, cuenta cuántas veces aparece el número 3 en la tupla.
numeros = (1, 3, 5, 3, 7, 3, 9)
conteo = numeros.count(3)
print("El número 3 aparece", conteo, "veces en la tupla.")

# 3️⃣ Crea una función que reciba una tupla con números y devuelva una nueva tupla con los números ordenados de menor a mayor.
def ordenar_tupla(tupla_numeros):
    return tuple(sorted(tupla_numeros))

numeros_desordenados = (9, 3, 7, 1, 5)
numeros_ordenados = ordenar_tupla(numeros_desordenados)
print("Tupla ordenada:", numeros_ordenados)
