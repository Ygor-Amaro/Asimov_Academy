#desafio_07.py

"""
Crie um "jogo dos estados". Neste jogo, o jogador precisa responder o nome da capital de cada Estado do Brasil. 
    - O jogo deve perguntar ao usuário "Qual a capital do Estado X?", e checar se o usuário respondeu de forma correta. 
    - Após cada pergunta, o usuário pode escolher parar o jogo ou continuar para a próxima pergunta.
    - Quando o usuário decidir parar, ou quando todas as perguntas forem respondidas, o código mostra o número bruto e porcentagem de acertos.
"""

import random

estados_capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

acertos = 0
erros = 0
total_perguntas = 2 #len(estados_capitais)

# Cria uma lista com os estados e embaralha
estados = list(estados_capitais.keys())
random.shuffle(estados)

# Itera sobre os estados embaralhados
for estado in estados:
    capital = estados_capitais[estado]
    resposta = input(f"Qual a capital do estado {estado}? ")
    if resposta.strip().lower() == capital.lower():
        print("\nResposta correta!\n\n")
        acertos += 1
    else:
        erros += 1
        print(f"\nResposta incorreta! A capital de {estado} é {capital}.\n\n")
    
    if erros > total_perguntas:
        print(f"\nVocê perdeu {erros} vidas. Fim de jogo!\n")
        break
    else:
        print(f"Você tem {3 - erros} vidas restantes.\n")
    
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.strip().lower() != 's':
        print(f"\nFim de jogo, você acertou {acertos}.\n")
        break
print(f"Você acertou {acertos/total_perguntas}%.")