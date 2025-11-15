#Aulas do curso ASIMOV ACADEMY

#Desafio 02 - usuário e senha

"""
Desafio - crie um programa que:
    - Pede por um nome de usuário e uma senha.
    - Se ambos forem corretos, exibe uma mensagem de sucesso.
    - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente quando o usuário está incorreto, e quando a senha está incorreta
    - O usuário/senha "corretos" podem ser definidos como variávies dentro do próprio código.
"""

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
