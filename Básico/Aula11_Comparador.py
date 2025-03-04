"""
Comparador de Dois Números
Usando comparadores básicos : <,> e =  
 
"""

n1 = int(input('Entre com o primeiro número: ')) 
n2 = int(input('Entre com o segundo número: '))

if n1 > n2 : print (f'{n1} é maior que {n2}')
elif n2 > n1 : print (f'{n2} é maior que {n1}')
else: print (f'{n1} é igual a  {n2}')