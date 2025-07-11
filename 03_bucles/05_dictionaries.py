###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

import os
os.system("cls")

# ejemplo tipico de diccionario
persona = {
  "nombre": "marc",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitterx": "@marcesteveg",
    "github": "@MarcEsteve",
    "linkedin": "Marc Esteve Garcia"
  }
}

# para acceder a los valores
# print(persona["nombre"]) # "marc"
# print(persona["edad"]) #25
# print(persona["calificaciones"][2])
# print(persona["socials"]["twitterx"])

# cambiar valores al acceder
# persona["nombre"] = "esteve"
# persona["calificaciones"][2] = 10

# eliminar completamente una propiedad
# del persona["edad"]
# print(persona)

# es_estudiante = persona.pop("es_estudiante") 
# print(f"es_estudiante: {es_estudiante}")
# print(persona)

# sobreescribir un diccionario con otro diccionario
# a = { "name": "marc", "age": 25 }
# b = { "name": "daniel", "es_estudiante": False }
# print(a)
# a.update(b)
# print(a)

# comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True

# obtener todas las claves
print("\nkeys:")
print(persona.keys())
print(persona["socials"].keys())

# obtener todas los valores
print("\nvalues:")
print(persona.values())

# obtener tanto clave como valor
print("\nitems:")
print(persona.items())

for key, value in persona.items():
  print(f"{key}: {value}")