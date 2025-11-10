#Aulas do curso ASIMOV ACADEMY

#Desafio 01

nome = input("Digite o seu nome: ")
idade = input("digite a sua idade: ")
nome_tamanho = len(nome)
idade_futuro = int(idade) + 5

print(f"Olá {nome}, o seu nome tem {nome_tamanho} letras e daqui 05 anos você terá: {idade_futuro} anos de idade")

#Desafio 02 - usuário e senha

usuario_sis = "ygor"
senha_sis = 123456
usario_dig = input("Digite o seu usuário\n: ")
senha_dig = int(input("Digite a sua senha\n: "))

if usario_dig != usuario_sis and senha_dig !=senha_sis:
    print("usuário e senha incorretos!")
elif usario_dig == usuario_sis and senha_dig !=senha_sis:
    print("senha incorreta!")
elif usario_dig != usuario_sis and senha_dig ==senha_sis:
    print("usuário incorreto!")
else:
    print("acesso permitido!")

#Desafio 03 - jogo do número secreto

vidas = 0
numero = 5
palpite = None

while vidas < 3 and numero != palpite:
    palpite = int(input("Digite um número de 0 - 10 para advinhar o número secreto\n:"))

    if palpite < numero:
        print("O número secreto é maior que o seu chute")
        vidas += 1
        print(f"Vidas restantes: {3 - vidas}")

    elif palpite > numero:
        print("O número secreto é menor que o seu palpite")
        vidas += 1
        print(f"Vidas restantes: {3 - vidas}")
    else:
        print("Parabéns!!! Você acertou o número secreto!!!")

if palpite != numero:
    print(f"Você perdeu X(. O número era {numero}.")