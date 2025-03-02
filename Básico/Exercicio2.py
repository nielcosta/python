""" 
IMC 
Indice de massa corporal 


"""

nome = input ('Escreva seu nome : ')
idade = input ('Escreva sua idade : ')
peso = float(input ('Escreva seu peso : '))
altura =  float(input ('Escreva sua altura : '))

imc = peso / (altura ** 2)

print(f"{nome}, seu IMC é de {imc:.2f}")

#IMC menor que 18,5: Magreza
if (imc < 18.5): print ('Você está com alto nível de Magreza. Cuidado !')

#IMC entre 18,5 e 24,9: Peso normal
elif (imc >=18.5 and imc <24.9): print ('Você está com peso normal')

#IMC entre 25,0 e 29,9: Sobrepeso
elif (imc >=25 and imc <29.9): print ('Você está com Sobrepeso. Cuidado! ')
#IMC entre 30,0 e 34,9: Obesidade grau I
elif (imc >=30 and imc <34.9): print ('Você está com Obesidade grau I.' )

#IMC entre 35,0 e 39,9: Obesidade grau II
elif (imc >=35 and imc <39.9): print ('Você está com Obesidade grau II.' )

#IMC maior que 40,0: Obesidade grau III
else: print ('Você está com Obesidade grau III.' )