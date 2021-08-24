import rpa as r
import pyautogui as pg
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
pg.sleep(2)
janela = pg.getActiveWindow()
janela.maximize()
dolar_comercial = r.read('(//input[@id="comercial"])[1]')

r.close()

#texto do email
texto_email = 'Valor dolar comercial ' + str(pd.Timestamp('today')) + ' : ' +  dolar_comercial

# email remetente, senha, destinatário
de = 'email_origem'
senha = '********'
para = 'email_destino'
#para02 = ''

# Setup the MIME
message = MIMEMultipart()
message['From'] = de
message['To'] = para
#message['To'] = para02
message['Subject'] = 'Cotação do dolar'   #Título do e-mail

# Corpo do E-mail com anexos
message.attach(MIMEText(texto_email, 'plain'))

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
session.starttls()  # Habilita a segurança
session.login(de, senha)  # Login e senha de quem envia o e-mail
texto = message.as_string()
session.sendmail(de, para, texto)
session.quit()
