print('*** Cálculo de taxa basal ***')
print('-----------------------------')

'''
Fórmula da taxa de metabolismo basal:

- HOMEM: 66 + (13,7 * peso) + (5 * Altura) - (6,8 * idade)
- MULHER: 665,1 + (9,56 * peso) + (1,8 * Altura) - (4,7 * idade)

'''
peso = input('Digite o seu peso(KG): ').strip()
peso_float = float(peso)

altura = input('Digite a sua altura(cm): ').strip()
altura_float = float(altura)

idade = input('Digite a sua idade(anos): ').strip()
idade_int = int(idade)

print('Qual é o seu gênero biológico? *Escolha 1 ou 2*')
genero = input('1 - Homem \n2 - Mulher\n').strip()
genero_int = int(genero)

if genero_int == 1:
    taxaMetabolicaBasal = 66 + (13.7 * peso_float) + (5 * altura_float) - (6.8 * idade_int)
elif genero_int == 2:
    taxaMetabolicaBasal = 665.1 + (9.56 * peso_float) + (1.8 * altura_float) - (4.7 * idade_int)
else:
    print('Gênero inválido')
    
print(f'Taxa de metabolismo basal: {taxaMetabolicaBasal:.2f}')