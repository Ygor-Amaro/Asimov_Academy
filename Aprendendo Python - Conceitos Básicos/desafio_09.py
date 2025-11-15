#desafio 09 - Baralho de Cartas

"""
Crie um código que simula um baralho de cartas.

O código deve conter as seguintes funções:
    - gerar_baralho -> retorna um baralho novo. Parâmetros da função
    - definem quantas cópias retornar (1 baralho, 2 baralhos, ...), se o baralho deve conter coringas, e se deve ser embaralhado antes de ser retornado.
    - mostrar_baralho -> exibe a quantidade de cartas no baralho e mostra quais são.
    - dar_as_cartas -> distribui as cartas do baralho entre X jogadores, de forma que cada jogador recebe Y cartas.
    - mostrar_jogadores -> exibe a quantidade de cartas na mão de cada jogador e mostra quais são.

A partir dessas funções, o código deve:
    - gerar o baralho e exibi-lo
    - dar as cartas para os jogadores
    - exibir o baralho aós as cartas terem sido distribuídas
    - exibir a mão de cada jogador

DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
DICA: utilize a função random.shuffle (módulo random) para embaralhar.
"""

def embaralhar_baralho(baralho: list) -> list:
    import random
    random.shuffle(baralho)
    return baralho

def gerar_baralho(n) -> list:
    cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    naipes = ['♠', '♥', '♦', '♣']
    
    baralho = []
    for naipe in naipes:
        for carta in cartas:
            baralho.append(f'{carta}{naipe}')
    return embaralhar_baralho(baralho*n)

def distribuir_cartas(baralho: list, num_jogadores: int, cartas_por_jogador: int) -> dict:
    return

qtd_baralhos = int(input('Quantos baralhos deseja gerar?\n'))
print(gerar_baralho(qtd_baralhos))

