import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo):
    # Configurações do servidor SMTP do Hotmail
    smtp_host = 'smtp-mail.outlook.com'
    smtp_port = 587
    smtp_usuario = 'firedashvcpc@outlook.com'  # Seu endereço de e-mail do Hotmail
    smtp_senha = 'firedash1910'     # Sua senha do Hotmail

    # Configuração do e-mail
    msg = MIMEMultipart()
    msg['From'] = smtp_usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Corpo da mensagem
    corpo_email = MIMEText(corpo, 'plain')
    msg.attach(corpo_email)

    # Conexão com o servidor SMTP
    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_usuario, smtp_senha)

        # Envio do e-mail
        server.sendmail(smtp_usuario, destinatario, msg.as_string())
        server.quit()

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")

# Exemplo de uso
if __name__ == '__main__':
    # Destinatário do e-mail
    destinatario = 'samuelsneres@gmail.com'

    # Assunto do e-mail
    assunto = 'teste e teste e teste'

    # Corpo do e-mail
    corpo_email = 'Gay, mas eu te amo.'

    # Envia o e-mail
    enviar_email(destinatario, assunto, corpo_email)
