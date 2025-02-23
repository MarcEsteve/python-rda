import imapclient
conxGmail = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conxGmail.login("marc.esteve.garcia@gmail.com","pass")


conxGmail.select_folder("INBOX") #Habitualmente es "INBOX" el nombre de la bandeja genérica de entrada


mail_bruto = conxGmail.fetch([4],['BODY[]', 'FLAGS']) #El primer parámetro es el número de mensaje a recuperar


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