#Aulas do curso ASIMOV ACADEMY

#Desafio 03 - jogo do número secreto

"""
Desafio - crie um programa que:
    - Escolhe um número secreto.
    - Pede por um chute do usuário.
    - Indica se o usuário acertou ou não.
    - Se não acertou, dá uma dica, dizendo
    - se o número é mais alto ou mais baixo.
    - Repete isso até 3 vezes!
"""

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