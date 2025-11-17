# Desafio 08 - Cifra de César

"""
Crie um código que implementa a "Cifra de César", isto é, que transforma um string movendo cada letra um certo número de passos no alfabeto. 
O número de passos é dado por uma chave.
Letra com acentos, espaços e pontuação permanecem iguais.

Exemplos:
    - "abc" com chave 1 = "bcd"
    - "ABCDE" com chave 2 = "CDEFG"
    - "Cachorro" com chave -1 = "Bzbgnqqn"
    - "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

DICA: construa 2 strings com as letras do alfabeto em ordem, um para letra minúsculas e outra para as maiúsculas, e use este string para guiar as substituições.
"""

alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifradecesar(texto, chave):
    resultado = ""

    for letra in texto:
        if letra in alfabeto_minusculo:
            indice_atual = alfabeto_minusculo.index(letra)
            novo_indice = (indice_atual + chave)
            resultado += alfabeto_minusculo[novo_indice]
        elif letra in alfabeto_maiusculo:
            indice_atual = alfabeto_maiusculo.index(letra)
            novo_indice = (indice_atual + chave)
            resultado += alfabeto_maiusculo[novo_indice]
        else:
            resultado += letra

    return resultado

texto = str(input("Digite o texto a ser criptografado: "))
chave = int(input("Digite a chave de criptografia (número de passos): ")) 
print(f"Texto criptografado:", cifradecesar(texto, chave))