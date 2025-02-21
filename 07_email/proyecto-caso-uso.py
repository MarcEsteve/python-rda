import win32com.client
import os
os.system("cls")

# Conectar a la aplicación de Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Acceder a la bandeja de entrada (6 es el código para la bandeja de entrada)
bandeja_entrada = outlook.GetDefaultFolder(6)

# Obtener los correos electrónicos de la bandeja de entrada
correos = bandeja_entrada.Items

# Ordenar los correos por fecha de recepción (descendente)
correos.Sort("[ReceivedTime]", True)

# Obtener el último correo
ultimo_correo = correos.GetFirst()

# Mostrar información del último correo
print(f"Asunto: {ultimo_correo.Subject}")
print(f"Remitente: {ultimo_correo.SenderName}")
print(f"Fecha de recepción: {ultimo_correo.ReceivedTime}")
print(f"Mensaje: {ultimo_correo.Body}")