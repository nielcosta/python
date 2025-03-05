""" 
IN OU NOT IN 
está contido ou não está contido.

"""
nomes= ['Daniel', 'Hugo', 'Ricardo', 'Miguel', 'Adam']
nome = input ('Entre com o usuario:')
if nome in nomes : print(f'{nome} foi encontrado na lista')
elif nome not in nomes: print(f'{nome} não foi encontrado na lista')
  