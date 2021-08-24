import schedule
from schedule import *
import time
from robot01 import Robot01
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd


def send_email(robot, erro):
        #texto do email
    texto_email = f'O bot {robot}  falhou: ' + str(pd.Timestamp('today')) + f'favor verificar. Erro: {erro}'

    # email remetente, senha, destinatário
    de = 'email_origem'
    senha = '********'
    para = 'destino'
    #para02 = ''

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = de
    message['To'] = para
    #message['To'] = para02
    message['Subject'] = f'Bot {robot} falha!!!!'   #Título do e-mail

    # Corpo do E-mail com anexos
    message.attach(MIMEText(texto_email, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
    session.starttls()  # Habilita a segurança
    session.login(de, senha)  # Login e senha de quem envia o e-mail
    texto = message.as_string()
    session.sendmail(de, para, texto)
    session.quit()



try:
    print('Iniciando.........')
    schedule.every().day.at("22:46").do(Robot01)
    while True:
        schedule.run_pending()
        time.sleep(1)

except IndexError as e:
    send_email('Robot01_Notepad', e)












