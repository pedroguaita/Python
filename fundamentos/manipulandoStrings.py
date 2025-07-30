frase = 'Curso em Video Python'  # cada letra e espaço recebe um índice e ocupa um espaço na memória.
'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
C u r s o   e m   V i  d  e  o      P  y  t  h  o  n
'''

# Acesso direto aos caracteres pelo índice
print(frase[0])   # C
print(frase[1])   # u
print(frase[2])   # r
print(frase[3])   # s
print(frase[4])   # o
print(frase[5])   # espaço
print(frase[6])   # e
print(frase[7])   # m
print(frase[8])   # espaço
print(frase[8])   # espaço (repetido propositalmente)
print(frase[8])   # espaço (repetido propositalmente)
print(frase[9])   # V
print(frase[10])  # i
print(frase[11])  # d
print(frase[12])  # e
print(frase[13])  # o
print(frase[14])  # espaço
print(frase[15])  # P
print(frase[16])  # y
print(frase[17])  # t
print(frase[18])  # h
print(frase[19])  # o
print(frase[20])  # n

# Escrever texto grande em apenas um print
print("""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa""")  # Exibe várias linhas de texto com um único print

# Fatiamento
print(frase[9:14])      # 'Video' → do índice 9 até o 13 (o índice final não é incluído).
print(frase[9:21:2])    # 'VeoPto' → do 9 ao 20, pulando de 2 em 2.
print(frase[:5])        # 'Curso' → do início (índice 0) até o índice 4.
print(frase[15:])       # 'Python' → do índice 15 até o final da string.
print(frase[9::3])      # 'VdPh' → do 9 até o final, pulando de 3 em 3.

# Análise
print(len(frase))                     # 21 → retorna o comprimento da string.
print(frase.count('o'))               # 3  → conta quantas vezes aparece a letra 'o' (minúscula).
print(frase.count('o', 0, 13))        # 1  → conta quantas vezes aparece 'o' do índice 0 ao 12.
print(frase.find('deo'))              # 11 → retorna o índice onde começa 'deo'.
print(frase.find('Android'))          # -1 → não encontrou, retorna -1.
print(frase.lower().find('video'))    # 9 → converte a frase para minúsculas e procura 'video' nela
print('curso' in frase)               # False → 'curso' minúsculo não está na string (está com 'C' maiúsculo).

# Transformação
print(frase.replace('Python', 'Android'))  # Substitui 'Python' por 'Android' → retorna nova string.
# frase = frase.replace('Python', 'Android')  # (opcional) atualizaria a variável com o novo conteúdo.
print(frase.upper())                       # Tudo em maiúsculo → 'CURSO EM VIDEO PYTHON'.
print(frase.lower())                       # Tudo em minúsculo → 'curso em video python'.
print(frase.capitalize())                  # Deixa só a primeira letra maiúscula e o restante minúsculo.
print(frase.title())                       # Deixa a primeira letra de cada palavra em maiúscula.

print(frase.upper().count('O'))            # Transforma tudo em maiúsculo e conta quantos 'O' existem → 3

frase3 = '   Curso em video  '
print(len(frase3.strip()))  # Remove espaços do início e do fim, depois mostra o comprimento da string limpa → 16

frase2 = '   Aprenda Python  '

print(frase2.strip())   # Remove todos os espaços do início e do fim da string → 'Aprenda Python'
print(frase2.rstrip())  # Remove somente os espaços do final (direita) → '   Aprenda Python'
print(frase2.lstrip())  # Remove somente os espaços do início (esquerda) → 'Aprenda Python  '

# Divisão
print(frase.split())    # Divide a string onde houver espaços → retorna uma lista com as palavras.
'''
 _________     ___     _________     ___________
|0 1 2 3 4|   |0 1|   |0 1 2 3 4|   |0 1 2 3 4 5|
|C u r s o|   |e m|   |V i d e o|   |P y t h o n|
     0          1          2              3
'''
dividido = frase.split()         # Armazena a lista ['Curso', 'em', 'Video', 'Python']
print(dividido[0])               # Curso → primeira palavra da lista
print(dividido[1])               # em → segunda palavra da lista
print(dividido[2])               # Video → terceira palavra da lista
print(dividido[3])               # Python → quarta palavra da lista

print(dividido[0][0])            # C → primeira letra da primeira palavra
print(dividido[0][1])            # u → segunda letra da primeira palavra

# Junção
print('-'.join(frase))  # Junta todos os caracteres da string, colocando '-' entre eles → 'C-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n'
