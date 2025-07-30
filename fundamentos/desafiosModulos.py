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

----------------------------------------------------------------------------------------------------------------------

'''
'''
#exercícios de módulos
----------------------------------------------------------------------------------------------------------------------
#ex016
from math import trunc
num = float(input('Digite um numero real: \n'))

print('O numero {} tem a parte inteira {}'.format(num, trunc(num)))
----------------------------------------------------------------------------------------------------------------------
#ex017

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = (co ** 2 + ca **2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))

#OU

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
----------------------------------------------------------------------------------------------------------------------

#ex018
import math
angulo = float(input('Digite o ângulo que você deseja calcular: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Ângulo digitado: {}'.format(angulo))
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))
----------------------------------------------------------------------------------------------------------------------

#ex019
import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)
print('Aluno escolhido: {}'.format(escolhido))
----------------------------------------------------------------------------------------------------------------------


#ex020

import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('Ordem de apresentação:')
print(lista)

#ex021

#import pygame
pygame.init()  #inicia o uso da biblioteca do pygame
pygame.mixer.music.load('nome do arquivo')
pygame.mixer.music.play()
input()
pygame,event.wait()
'''