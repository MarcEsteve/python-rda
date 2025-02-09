###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

import os
os.system("cls")

""" Definición de una función

def nombre_de_la_funcion(parametro1, parametro2, ...):
  # docstring
  # cuerpo de la función
  return valor_de_retorno # opcional

"""

# # Ejemplo de una función para imprimir algo en consola
def saludar():
  print("¡Hola!")

# saludar()

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#   print(f"¡Hola {nombre}!")

# saludar_a("marc")
# saludar_a("cristina")
# saludar_a("fernando")

# El parámetro es lo que acepta la función
# El argumento es el valor que se le pasa a la función 

# # Funciones con más parámetros
# def sumar(a, b):
#   suma = a + b
#   return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las funciones con docstring
def restar(a, b):
  """Resta dos números y devuelve el resultado"""
  return a - b
# En Python puedes acceder al docstring de una función con el atributo __doc__
# print(restar.__doc__)
# Incluso help(restar) te mostrará el docstring de la función
# help(restar)

# parámetros por defecto
# def multiplicar(a, b = 2):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
# describir_persona(1, 25, "gato")
# describir_persona("marc", 25, "gato")
# describir_persona("hombre", "marc", 39)

# Argumentos por clave
# parámetros nombrados
# describir_persona(sexo="gato", nombre="marc", edad=25)
# describir_persona(sexo="hombre", nombre="pedro", edad=21) 

# Argumentos de longitud de variable (*args):
# def sumar_numeros(*args):
#   suma = 0
#   for numero in args:
#     suma += numero
#   return suma

# print(sumar_numeros(1, 2, 3, 4, 5))
# print(sumar_numeros(1, 2))
# print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
# def mostrar_informacion_de(**kwargs):
#   for clave, valor in kwargs.items():
#     print(f"{clave}: {valor}")

# mostrar_informacion_de(nombre="marc", edad=25, sexo="gato")
# print("\n")
# mostrar_informacion_de(name="pedro", edad=21, country="Madagascar")
# print("\n")
# mostrar_informacion_de(nick="charly", es_sub=True, is_rich=True)
# print("\n")
# mostrar_informacion_de(super_name="juan", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora
# rangos, listas, bucles, etc.