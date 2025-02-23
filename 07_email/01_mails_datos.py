import imapclient
# connOutlook = imapclient.IMAPClient("imap-mail.outlook.com", ssl=True)
# connOutlook.login("arthas_003@hotmail.com","pass")

# YAHOO imap.mail.yahoo.com
# HOTMAIL imap-mail.outlook.com
# ZOHO imap.zoho.com
# AT&T imap.mail.att.net
# ICLOUD imap.mail.me.com
# AOL imap.aol.com
# Comcast imap.comcast.net
# Verizon incoming.verizon.net
# GMAIL imap.gmail.com
# OUTLOOK imap-mail.outlook.com
# OFFICE365 outlook.office365.com
conxGmail = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conxGmail.login("marc.esteve.garcia@gmail.com","pass")


conxGmail.select_folder("INBOX") #Habitualmente es "INBOX" el nombre de la bandeja genérica de entrada


# Buscar mensajes cuyo asunto contenga "WordPress"
UIDs_asunto = conxGmail.search(['SUBJECT', 'WordPress'])

if UIDs_asunto:
    # Recuperar el contenido del primer mensaje encontrado
    mail_bruto = conxGmail.fetch([UIDs_asunto[0]], ['BODY[]', 'FLAGS'])
    print(mail_bruto)
else:
    print("No se encontraron mensajes con el asunto 'WordPress'.")

if UIDs_asunto:
    try:
        # Recuperar el contenido del primer mensaje encontrado
        mail_bruto = conxGmail.fetch([UIDs_asunto[0]], ['BODY[]', 'FLAGS'])
        mensaje = mail_bruto[UIDs_asunto[0]][b'BODY[]'].decode("utf-8")
        print(mensaje)
    except KeyError:
        print("No se pudo encontrar el cuerpo del mensaje.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
else:
    print("No se encontraron mensajes con el asunto 'WordPress'.")

mensaje.find("smtp.mailfrom=")

# Me devuleve mensaje.find("smtp.mailfrom=") un -1 porque no lo encuentra

# Cerrar la conexión
conxGmail.logout()


