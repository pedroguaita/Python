'''
#import math -> import genérico.

from math import sqrt, floor
num = int(input('Digite um número: \n'))

#raiz = math.sqrt(num) -> apenas quando faço a importação genérica.

raiz = sqrt(num)

#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) -> apenas quando faço a importação genérica.
#print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) -> apenas quando faço a importação genérica.
#print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

# import + "Ctrl" + "espaço" vai abrir um leque de opções de bibliotecas
import random
num = random.randint(1, 10)  #randint gera números inteiros aleatórios, os () sao os parametros
print(num)
'''

#exercícios de módulos
#----------------------------------------------------------------------
#ex016
from math import trunc

num = float(input('Digite um numero real: \n'))

print('O numero {} tem a parte inteira {}'.format(num, trunc(num)))
#----------------------------------------------------------------------

#ex017

co = float(input('Cateto oposto: '))
ca = float (input('Cateto adjascente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'Hipotenusa: {hi:.2f}')

#ou
from math import hypot
co = float(input('Cateto oposto: '))
ca = float (input('Cateto adjascente: '))
hi = hypot(co, ca)
print(f'Hipotenusa: {hi:.2f}')
#----------------------------------------------------------------------

#ex018
from math import radians, sin, cos, tan
an = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians)
cos = cos(radians)
tan = tan(radians)

print(f'O angulo de {an}° tem o seno de {seno:.2f}')
print(f'O angulo de {an}° tem o cosseno de {cos:.2f}')
print(f'O angulo de {an}° tem o cosseno de {tan:.2f}')
#----------------------------------------------------------------------

#019
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1,n2,n3,n4]

escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')

#020

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]

shuffle(lista)
print(f'Ordem de apresentação: {lista}')