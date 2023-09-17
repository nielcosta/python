import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import tkinter as tk
from tkinter import filedialog

def capturar_clientes(nome_arquivo):
    try:
        workbook = openpyxl.load_workbook(nome_arquivo)
        sheet = workbook.active
        clientes = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            nome = row[0]
            email = row[1]
            clientes.append((nome, email))

        workbook.close()
        return clientes

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return []

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()
    arquivo = filedialog.askopenfilename()
    return arquivo

def enviar_email(destinatario, assunto, corpo_email, assinatura, anexo):
    remetente = 'danielmendes.dsr@gmail.com'
    senha = 'nleafbxtzdrezdrl'

    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto

    corpo = corpo_email + "\n\n" + assinatura
    mensagem.attach(MIMEText(corpo, 'plain'))

    if anexo:
        # Abre o arquivo e o adiciona como anexo
        with open(anexo, 'rb') as arquivo:
            anexo_mime = MIMEBase('application', 'octet-stream')
            anexo_mime.set_payload(arquivo.read())
            encoders.encode_base64(anexo_mime)
            anexo_mime.add_header('Content-Disposition', f'attachment; filename="{anexo}"')
            mensagem.attach(anexo_mime)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as servidor_smtp:
            servidor_smtp.starttls()
            servidor_smtp.login(remetente, senha)
            servidor_smtp.sendmail(remetente, destinatario, mensagem.as_string())
        print(f"E-mail enviado para {destinatario} com sucesso!")
    except smtplib.SMTPException as e:
        print(f"Erro ao enviar e-mail para {destinatario}: {str(e)}")

def main():
    nome_arquivo = r'E:\Python\Robos Python\Secao92\clientes.xlsx'
    clientes = capturar_clientes(nome_arquivo)

    if clientes:
        assunto = input("Digite o assunto do e-mail: ")
        corpo_email = input("Digite o corpo do e-mail: ")
        assinatura = "Atenciosamente,\nSua assinatura"

        print("Selecione o arquivo a ser anexado:")
        anexo = selecionar_arquivo()

        for cliente in clientes:
            nome, email = cliente
            enviar_email(email, assunto, corpo_email, assinatura, anexo)

if __name__ == '__main__':
    main()
