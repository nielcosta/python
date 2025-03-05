""" 
Exercício 
Peça ao usuário digitar o seu nome: 
PEça ao usuario digitar sua idade:
Se o nome e idade foram digitados :
Exiba : 
Seu nome é (nome).
Seu nome invertido .
Se no nome contém espaços. 
Quantas letras .
Mostre a primeira letra
Mostre a última letra
Se nada for digitado em nome ou idade : Exiba , você deixou campos vazios. 

"""    
#Resolução 

#Peça ao usuário digitar o seu nome: 
nome = input ('Digite o seu nome:')

#PEça ao usuario digitar sua idade:
idade = input ('Digite a sua idade: ')
         
#Se o nome e idade foram digitados :
#Se nada for digitado em nome ou idade : Exiba , você deixou campos vazios.

if nome =='' or idade == '': print ('Há campos que faltam ser preenchidos!')

else:
    #Seu nome é (nome).
    print (f'Seu nome :{nome}')

    #Seu nome invertido .
    print (f' Seu nome invertido:{nome[::-1]}')
    
    #Se no nome contém espaços.
    if ' ' in nome:
     print('O nome possui espaços.')
    
     # Quantas letras.
    print(f'Quantidade de caracteres: {len(nome)}')
    
    #Mostre a primeira letra
    print(f'Primeira Letra : {nome[0]}')
    
    #Mostre a última letra
    print(f'Última Letra : {nome[-1]}')
