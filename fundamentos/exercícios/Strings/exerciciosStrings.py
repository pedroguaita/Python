
#ex01
nome = str(input('Digite seu nome:')).strip()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

#OU

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
#-------------------------------------------------------------------------------------------------------------------

print(f'O seu nome tem {len(nome) - nome.count(' ')} letras')  #tamanho da string - (menos) os espaços contados

#-------------------------------------------------------------------------------------------------------------------
print(f'O primeiro nome tem {nome.find(' ')} letras')
#OU
separa = nome.split()
print(separa)
print(f'Seu primeiro nome é {separa[0]} e possui {len(separa[0])} letras')

#ex02
numero = int(input('Digite um numero: '))
uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10

print(f'Unidade: {uni}\nDezena: {dez}\nCentena: {cen}\nMilhar:{mil}')

#ex03
#verificando as primeiras letras de um nome
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade.capitalize()[:5] == 'Santo')

#ex04
nome = str(input('Digite o seu nome: ')).strip()
print(f'Seu nome tem Silva? {'Silva' in nome.lower()}')

#ex05

frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A apareceu {frase.count('a')} vezes')
print(f'A letra A aparece a primeira vez na posição {frase.find('a')+1}')
print(f'A letra A aparece pela última vez na posição {frase.rfind('a')+1}')

#ex06

nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Nome completo: {nome}')
separado = nome.split()
print(f'Primeiro nome: {separado[0]}')
print(f'Último nome: {nome[len(nome)-1]}')

