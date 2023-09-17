# Loop para conversar com o modelo
print("Bem-vindo ao ChatGPT! Digite 'sair' para encerrar a conversa.")
while True:
    pergunta = input("Você: ")

    if pergunta.lower() == 'sair':
        break

    resposta = obter_resposta(pergunta)
    print("ChatGPT:", resposta)