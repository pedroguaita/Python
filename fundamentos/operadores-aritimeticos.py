'''

Operadores relacionais

5**2 potencia
ou 
pow (5,2)

Raiz quadrada

81**(1/2)

raiz cubica

127**(1/2)

print('Oi' + 'Olá')**5

print('='*20)
-------------------------------------------------------------------------------
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

ou

nome = str(input('Qual é seu nome? '))
print('Prazer em te conhecer {:20}!'.format(nome)) #utilizou 20 espaços

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome)) #alinhou a direita 20 espaços

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome)) #centralizado

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome)) #centralizado com '=' em volta

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print ('a soma vale {}'.format(n1+n2))
'''
#Ou

n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
soma = n1 + n2
subtr = n1 - n2
multi = n1 * n2
div = n1 / n2
divInteira = n1 // n2
expo = n1 ** n2
raizN1 = n1 **(1/2)
raizN2 = n1 **(1/2)
'''
print('A soma = {}'.format(soma))
print('A subtração = {}'.format(subtr))
print('A multiplicação = {}'.format(multi))
print('A divisão = {:.2f}'.format(div)) #para limitar as casas decimais {:.Numerof}
print('A divisão inteira = {}'.format(divInteira))
print('A potência do número 1 elevado ao número 2 = {}'.format(expo))
print('A raiz do número 1 = {}'.format(raizN1))
print('A raiz do número 2 = {}'.format(raizN2))
'''
#para não quebra a linha se utiliza (,end=' ')
#para quebrar é só por um '/n' igual a linguagem C.

#exemplo

print('A soma é {}, o produto é {}, e a divisão é {:.1f}'.format(soma, multi, div), end=' ')
print('Divisão inteira {} e potência {}'.format(divInteira, expo))


