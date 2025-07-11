###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

import os
os.system("cls") # limpia la pantalla

# print("\n Bucle while:")

# Bucle con una simple condición
# contador = 0

# {llaves} [corchete] (parentesis)
# indentación "tabulación o sangrado"

# while contador <= 5:
#     print(contador)
#     contador += 1 # es super importante para evitar un bucle infinito

# utilizando la palabra break, para romper el bucle
# print("\n Bucle while con break:")
# contador = 0

# while True:
#   print(contador)
#   contador += 1
#   if contador == 5:
#     break # sale del bucle

# continue, que lo hace es saltar esa iteración en concreto
# y continuar con el bucle
# print("\n Bucle con continue")
# contador = 0
# while contador < 10:
#   contador += 1

#   if contador % 2 == 0:
#     continue

#   print(contador)

# else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1

# else:
#   print("El bucle ha terminado, y ha recorrido todos los números")

# else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1
# else:
#   print("El bucle ha terminado")

# contador = 0
# while contador < 5:
#     print(f"Contador es {contador}")
#     contador += 1
# else:
#     print("El bucle while ha terminado de forma natural.")
#     print(f"El valor final del contador es {contador}.")

# numero = 0
# while numero < 10:
#     print(f"Número es {numero}")
#     if numero == 3:
#         print("¡Hemos alcanzado el 3! Rompiendo el bucle.")
#         break  # Interrumpe el bucle
#     numero += 1
# else:
#     print("Este mensaje no se imprimirá porque el bucle fue interrumpido por 'break'.")

# print("El programa ha continuado después del bucle.")

# Salida esperada:
# Número es 0
# Número es 1
# Número es 2
# Número es 3
# ¡Hemos alcanzado el 3! Rompiendo el bucle.
# El programa ha continuado después del bucle.

# Salida esperada:
# Contador es 0
# Contador es 1
# Contador es 2
# Contador es 3
# Contador es 4
# El bucle while ha terminado de forma natural.
# El valor final del contador es 5.

# pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
# numero = -1
# while numero < 0:
#   numero = int(input("Escribe un número positivo: "))
#   if numero < 0:
#     print("El número debe ser positivo. Intenta otra vez, majo o maja.")

# print(f"El número que has introducido es {numero}")

# numero = -1
# while numero < 0:
#   try:
#     numero = int(input("Escribe un número positivo: "))
#     if numero < 0:
#       print("El número debe ser positivo. Intenta otra vez, majo o maja.")
#   except:
#     print("Lo que introduces debe ser un número, que si no peta!")

# print(f"El número que has introducido es {numero}")

###
# EJERCICIOS (while)
###

# # Ejercicio 1: Cuenta atrás
# # Imprime los números del 10 al 1 usando un bucle while.
# print("\nEjercicio 1:")

# # Ejercicio 2: Suma de números pares (while)
# # Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print("\nEjercicio 2:")

# # Ejercicio 3: Factorial de un número
# # Pide al usuario que introduzca un número entero positivo.
# # Calcula su factorial usando un bucle while.
# # El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# # 5! = 5 x 4 x 3 x 2 x 1 = 120.
# print("\nEjercicio 3:")

# # Ejercicio 4: Validación de contraseña
# # Pide al usuario que introduzca una contraseña.
# # La contraseña debe tener al menos 8 caracteres.
# # Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# # Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")

# # Ejercicio 5: Tabla de multiplicar
# # Pide al usuario que introduzca un número.
# # Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")

# # Ejercicio 6: Números primos hasta N
# # Pide al usuario que introduzca un número entero positivo N.
# # Imprime todos los números primos menores o iguales que N usando un bucle while.
# print("\nEjercicio 6:")