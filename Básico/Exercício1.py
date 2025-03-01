from datetime import datetime

# Solicitar informações ao usuário
nome = input('Entre com o seu nome: ')
sobrenome = input('Entre com o seu sobrenome: ')
data_nascimento = input('Entre com a data de nascimento (dd/mm/aaaa): ')

# Converter a data de nascimento para um objeto datetime
data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

# Calcular a idade da pessoa
hoje = datetime.today()
idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

# Exibir a idade da pessoa
print(f'{nome} {sobrenome}, você tem {idade} anos.')

if idade >=18: print('Você é maior de idade!')
else:print('Você é menor de idade!')

