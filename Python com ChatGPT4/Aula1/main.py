import openai

# Defina a sua chave de API da OpenAI
openai.api_key = "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"

# Função para enviar a pergunta e receber a resposta do modelo
def obter_resposta(pergunta):
    resposta = openai.Completion.create(
        engine='gpt-3.5-turbo',  # Especifica o modelo do ChatGPT a ser usado
        prompt=pergunta,
        max_tokens=50,  # Define o limite de tamanho da resposta
        temperature=0.7,  # Controla a aleatoriedade da resposta (quanto maior, mais aleatória)
        n=1,  # Define o número de respostas para retornar
        stop=None,  # Define as palavras para encerrar a resposta, se desejado
        timeout=30  # Define o tempo limite em segundos para a solicitação
    )

    return resposta.choices[0].text.strip()

# Loop para conversar com o modelo
print("Bem-vindo ao ChatGPT! Digite 'sair' para encerrar a conversa.")
while True:
    pergunta = input("Você: ")

    if pergunta.lower() == 'sair':
        break

    resposta = obter_resposta(pergunta)
    print("ChatGPT:", resposta)