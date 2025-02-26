import smtplib #pip install secure-smtplib

# Configuración del servidor
con = smtplib.SMTP("smtp.gmail.com", 587)

#Iniciar conexión
con.ehlo() 
con.starttls() # Conexion segura encriptada

con.login("marc.esteve.garcia@gmail.com","lwlj sygs krqg shlb") #Insertar contraseña de aplicaciones

#Envío de emails
con.sendmail("marc.esteve.garcia@gmail.com", "arthas_003@hotmail.com", "Subject: Prueba\n\nHola, esto es una prueba")