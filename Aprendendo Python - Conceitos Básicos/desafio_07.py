#desafio_07.py

"""
Crie um "jogo dos estados". Neste jogo, o jogador precisa responder o nome da capital de cada Estado do Brasil. 
    - O jogo deve perguntar ao usuário "Qual a capital do Estado X?", e checar se o usuário respondeu de forma correta. 
    - Após cada pergunta, o usuário pode escolher parar o jogo ou continuar para a próxima pergunta.
    - Quando o usuário decidir parar, ou quando todas as perguntas forem respondidas, o código mostra o número bruto e porcentagem de acertos.
"""

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

quer_continuar = True
acertos = 0
rodadas = 0


for estado, capital in estados_capitais.items():
    if not quer_continuar:
        break
    rodadas += 1

    print(f"\nQual a capital do estado {estado}?")

    resposta = input("Sua resposta: ")
    if resposta.lower() == capital.lower():
        print("Resposta correta!\n")
        acertos += 1
    else:
        print(f"Resposta incorreta! A capital de {estado} é {capital}.\n")

    while True:
        opcao = input("Deseja continuar? (s/n): ").lower()
        if opcao not in ['s', 'n']:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
            continue
        elif opcao == 'n':
            print(f"Você acertou {acertos/rodadas*100}%\nObrigado por jogar!")
            quer_continuar = False
        break