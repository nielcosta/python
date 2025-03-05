""" 
Função OR
Irá funcionar caso uma das opções seja verdadeira. 

"""

nome = input ('Entre com o usuario:')
senha_digitada = input ('Entre com a senha :')

usuario ='admin'
senha = 'admin'

if ((nome == usuario) or (nome =='Daniel')) and ((senha_digitada == senha) or (senha_digitada =='')) :
    print ('Entrada permitida!')
elif  not (nome == 'Daniel') : print ('VocÊ não é Daniel !') 
else : print ('Entrada não permitida!')