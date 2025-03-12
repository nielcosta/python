"""
    Exercicio 1 
    Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar.
    Caso o usuário não digite um número inteiro , informe que não é número inteiro.    

try:
    num = int(input('Digite um número :'))
    if (num % 2 == 0): print(f'{num} é par.')
    else: print(f'{num} é ímpar.')
except: print('Você não digitou um número inteiro!')    

"""
"""
Exercício 2 
Faça um programa que pergunte a hora ao usuário e baseando-se no horário descrito utilize a saudação 
apropriada.


try:
    horario = input('Digite as horas (HH:mm) :')
    horas = int(horario[:2])
    
    dia = (horas >= 0) and (horas <12)
    tarde = (horas >= 12) and (horas < 18)
        
    if dia : print(f'Horário :{horario}. Bom dia !')
    elif tarde: print(f'Horário :{horario}. Boa tarde!')
    else: print(f'Horário :{horario}. Boa noite!')
    
except: print('Você não digitou um horário válido!')  

"""
"""
Exercício 3 
Faça um programa que pergunte o nome do usuário e caso o nome tenha menos que 4 letras informe que o nome
é curto. Se o nome tiver entre 5 e 6 caracteres informe que este nom tem tamanho normal e caso exceda a 6 coloque 
nome Comprido. 

"""


try:
    nome = input('Digite seu nome: ')

    if len(nome) < 4:
        print(f'{nome}, seu nome é muito curto!')
    elif len(nome) <= 6:  # Esta condição já cobre nomes curtos de até 6 caracteres
        print(f'{nome}, seu nome é curto!')
    else:
        print(f'{nome}, seu nome é muito grande!')
except Exception as e:  # É uma boa prática especificar o tipo de exceção ou capturá-la para debugging
    print('Você não digitou um nome válido!')
