'''
# exercício 001

print ('Hello World\n')

#exercício 002

nome = input('Digite o seu nome:\n')
print('Seja Bem-Vindo, {}!\n'.format(nome))

#OU

nome = input('Digite seu nome:\n')
print('Seja Bem-Vindo,',nome,'!')

#exercício 003

n1 = int(input('Digite o primeiro número:\n'))
n2 = int(input('Digite o segundo número:\n'))
soma = n1 + n2
print('A soma dos números é:',soma)

n1 = int(input('Digite o primeiro número:\n'))
n2 = int(input('Digite o segundo número:\n'))
soma = n1 + n2
print('A soma do número {} + {} = {}:'.format(n1, n2, soma))
'''
#exercício 004

var = input('Digite algo:\n')
print('O tipo primitivo desse valor é ', type(var))
print('Só tem espaços?', var.isspace())
print('É um número? ', var.isnumeric())
print('É alfabético? ', var.isalpha())
print('É alfanumérico? ', var.isalnum())
print('Está em maiúsculas? ', var.isupper())
print('Está em minúsculas? ', var.islower())
print('Está capitalizada? ', var.istitle())










