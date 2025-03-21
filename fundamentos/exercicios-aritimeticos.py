'''
#ex 005
num = int((input('Digite um valor: \n')))
print('O ANTECESSOR de {} é {}. Já o SUCESSOR de {} é {}'.format(num, num - 1, num, num + 1))

#006

num = int(input('Digite um valor: \n'))
dobro = num * 2
triplo = num * 3
raiz = num**(1/2)
print('O dobro de {} é {}'.format(num, dobro))
print('O triplo de {} é {}'.format(num, triplo))
print('A riaz quadrada de {} é {:.1f}'.format(num, raiz))


#ex 07

nota1 = float(input('Insira a nota 1: \n'))
nota2 = float(input('Insira a nota 2: \n'))
media = (nota1 + nota2) / 2
print('A média final é {}'.format(media))


#ex 008

num = float(input('Insira a medida em metros: \n'))
centimetros = num * 100
milimetros = num * 1000
print('{} metro(s) é equivalente a {} centímetro(s).'.format(num, centimetros))
print('{} metro(s) é equivalente a {} milímetro(s).'.format(num, milimetros))


#ex 009 (formar uma tabuada apenas com comandos sequenciais e aritiméticos, sem o uso de um laço de repetição)

num = int(input('Digite um número para formar uma tabuada: \n'))
print('{} x 0 = {}'.format(num, num*0))
print('{} x 1 = {}'.format(num, num*1))
print('{} x 2 = {}'.format(num, num*2))
print('{} x 3 = {}'.format(num, num*3))
print('{} x 4 = {}'.format(num, num*4))
print('{} x 5 = {}'.format(num, num*5))
print('{} x 6 = {}'.format(num, num*6))
print('{} x 7 = {}'.format(num, num*7))
print('{} x 8 = {}'.format(num, num*8))
print('{} x 9 = {}'.format(num, num*9))
print('{} x 10 = {}'.format(num, num*10))

#ex 010

reais = float(input('Quantos reais você tem?\n'))
conversao = reais / 5.00 #exemplo
print('Você possui ${:.2f}.'.format(conversao))

#011

alt = float(input('Insira a altura da parede(em metros):\n'))
largura = float(input('Insira a largura da parede(em metros):\n'))
area = alt * largura
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))


#ex 012

preco = float(input('Insira o preço:\n'))
desconto = preco * 0.05
print('O valor com 5% de desconto é de {}!'.format(preco - desconto))

#013

sal = float(input('Insira o seu salário atual:\n'))
sal_novo = sal*0.15 + sal
print('O seu novo salário, com um aumento de 15% é de {}!'.format(sal_novo))

#014

c = float(input('Informe a temperatura em °C: \n'))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
'''

#ex 015

km = float(input('Informe a quantidade de Km´s percorridos:\n' ))
dias = int(input('Informe a quantidade de dias em que o carro ficou alugado:\n'))
custo = ((dias * 60) + (km * 0.15))
print('O total a pagar é de {:.2f}'.format(custo))

