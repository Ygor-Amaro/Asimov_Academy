#Aulas do curso ASIMOV ACADEMY

#Desafio 04
"""
Dado uma sequência de números, calcule a soma e média dos números.
ATENÇÃO: não vale usar a função sum() !

Dado uma sequência de números, calcule o maior valor da sequência.
ATENÇÃO: não vale usar a função max() !

Dado uma lista de palavras, printe todas as palavras
com pelo menos 5 caracteres.
"""


# Calcular soma e média
lista_numeros = [1, 2, 3, 4, 5]
soma = 0
media = 0

for n in lista_numeros:
    soma += n
    media = soma / len(lista_numeros)
print(f'Soma: {soma}')
print(f'Média: {media}')


# Encontrar o maior número
maior = lista_numeros[0]

for n in lista_numeros[1:]:
    if n > maior:
        maior = n
print(f'Maior número: {maior}')


# Printe palavras com pelo menos 5 caracteres
lista_palavras = ['Jujubinha', 'casa', 'bola', 'computador', 'pão', 'carro']

for palavra in lista_palavras:
    if len(palavra) >= 5:
        print(palavra)