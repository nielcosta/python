""" 
Função AND
Só irá funcionar caso todas as opções sejam verdadeiras. 

"""

nome = input ('Entre com o usuario:')
senha_digitada = input ('Entre com a senha :')

usuario ='admin'
senha = 'admin'

if (nome == usuario) and (senha_digitada == senha): print ('Entrada permitida!')
else : print ('Entrada não permitida!')