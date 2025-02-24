import imapclient # pip install imapclient
#Conexión y descarga
con = imapclient.IMAPClient("imap.gmail.com", ssl=True)

con.login("marc.esteve.garcia@gmail.com","pass") #Insertar contraseña de aplicaciones

con.select_folder("INBOX") #Habitualmente es "INBOX" el nombre de la bandeja genérica de entrada

# Filtrar por fecha
UIDS = con.search(['SINCE', '01-Jan-2025'])

# Filtrar por no leídos
UIDS_no_leidos = con.search(['UNSEEN'])

print(UIDS_no_leidos) # Lista de mensajes no leídos "UIDS_no_leidos" en Jupyter los muestra

# Descargar los mensajes no leídos
for uid in UIDS_no_leidos:
    mail = con.fetch([uid], ['BODY[]', 'FLAGS'])
    print(mail)


# Cerrar la conexión
con.logout()

