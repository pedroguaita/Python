tempo = int(input('Quantos anos tem o seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

#Ou

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'Carro velho')

#------------------------------------------------------#

nome = str(input('Qual é o seu nome? '))

if nome == 'Ronaldo':
    print(f'Siuuuuu')
else:
    print(';-;')
print(f'Bom dia, {nome}')

#------------------------------------------------------#

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2)/2
print(f'A sua media é de {media:.2f}')

if media >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')

#Ou

#print('Aprovado' if media >= 6.0 else 'Reprovado')
