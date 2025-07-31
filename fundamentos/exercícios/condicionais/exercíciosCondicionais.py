#ex01
from random import choice
lista = [0, 1, 2, 3 ,4 ,5]
escolhido = choice(lista)

num = int(input('Tente adivinhar um numero entre 0 e 5: '))

if num == escolhido:
    print(f'Acertou! Eu escolhi o numero {escolhido}.')
else:
    print(f'Errou! Eu escolhi o número {escolhido}.')
#ou
from random import randint
computador = randint(0, 5)
#print(f'Pensei no número {computador}')
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = input('Em que número pensei? ')
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}')
#---------------------------------------------------------
#02
velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7.00
if velocidade > 80:
    print(f'Parabéns, voce foi multado em R${multa:.2f}!')
else:
    print('Você está dentro do limite de velocidade!')
#---------------------------------------------------------
#ex03

num = int(input('Digite um numero e falarei se é par ou ímpar: '))

if (num % 2) == 0:
    print(f'O número {num} é PAR.')
else:
    print('Impar')
#---------------------------------------------------------#---------------------------------------------------------
#ex04
print('#----------------------------------------------------------------------------------#')
print('|Para viagens de até 200Km cobramos R$0,50 por KM e para viagens mais longas R$0,45|')
print('#----------------------------------------------------------------------------------#')
distancia = float(input('Informe a distância da viagem(KM): '))

if distancia <= 200.00:
    preco = distancia * 0.50
    print(f'O valor da viagem será de R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O valor da viagem será de R${preco:.2f}')
#---------------------------------------------------------
#ex05
from datetime import date
ano = int(input('Insira um ano para analisar e digite 0 para analisar o ano atual(exemplo-> 2025):  '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é um ano bissexto')
else:
    print('Não é um ano bissexto')
#---------------------------------------------------------
#ex06
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

# Verifica se todos são iguais
if n1 == n2 == n3:
    print('Todos os números são iguais.')
else:
    # Acha o maior
    if n1 >= n2 and n1 >= n3:
        maior = n1
    elif n2 >= n1 and n2 >= n3:
        maior = n2
    else:
        maior = n3

    # Acha o menor
    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3

    print(f'O maior número é {maior} e o menor é {menor}')
#---------------------------------------------------------
#resolução (teste)
n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o terceiro numero: '))

if n1 >= n2 and n1 >= n3 and n2 >= n3:
    print(f'O maior numero é o {n1} e o menor é o {n3}')
elif n2 >= n1 and n2 >= n3 and n1 >= n3:
    print(f'O maior numero é o {n2} e o menor é o {n3}')
elif n3 >= n1 and n3 >= n2 and n1 >= n2:
    print(f'O maior numero é o {n3} e o menor é o {n2}')
elif n1 <= n2 and n1 <= n3 and n2 <= n3:
    print(f'O maior numero é o {n3} e o menor é o {n1}')
elif n1 <= n2 and n1 <= n3 and n3 <= n2:
    print(f'O maior numero é o {n2} e o menor é o {n1}')
else:
    print('Os números são iguais.')

#Ou

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

if n1 == n2 == n3:
    print('Todos os números são iguais.')
else:
    print(f'O maior número é {maior} e o menor é {menor}')

#Ou

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

#menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n1:
    maior = n3
print(f'O maior número  é {maior} e o menor é {menor}')