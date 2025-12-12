# CÁLCULO DE IMC
# peso / (altura x altura)

nome =  'Pedro'
peso = 84
altura = 1.68
imc = peso / (altura ** 2)

print('Nome:', nome, 
    '\nPeso(KG):', peso, 
    '\nAltura:', altura,)

print((f'O seu IMC é de {imc:.2f}').replace('.', ','))