#Aulas do curso ASIMOV ACADEMY

#Desafio 01
"""
Desafio - crie um programa que:
    - Pede pelo seu nome e idade
    - Dá oi para você
    - Conta quantas letras seu nome possui
    - Fala quantos anos você terá daqui a 5 anos
"""

nome = input("Digite o seu nome: ")
idade = input("digite a sua idade: ")
nome_tamanho = len(nome)
idade_futuro = int(idade) + 5

print(f"Olá {nome}, o seu nome tem {nome_tamanho} letras e daqui 05 anos você terá: {idade_futuro} anos de idade")