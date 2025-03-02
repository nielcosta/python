""" 
Operadores Artméticos 

"""
n1 = int(input ("Digite um número: "))
n2 = int(input ("Digite o segundo número: "))

add  =    n1 + n2    #Adiçao
sub  =    n1 - n2    #Subtração 
mult =    n1 * n2    #Multiplicação
div  =    n1 / n2    #Divisão 
div_int = n1 // n2   #Divisao_inteira
exp  =    n1 ** n2   #Exponenciação
mod  =    n1 %  n2   #Módulo ou Resto da Divisão 

print(f'Adição:{n1} + {n2} = {add}')
print(f'Subtração:{n1} - {n2}= {sub}')
print(f'Multiplicação:{n1} * {n2}= {mult}')
print(f'Divisão:{n1} / {n2}= {div}')
print(f'Divisao Inteira: {n1} // {n2}= {div_int}')
print(f'Exponenciação:{n1} ** {n2}= {exp}')
print(f'Módulo: Resto de {n1} / {n2}= {mod}')
