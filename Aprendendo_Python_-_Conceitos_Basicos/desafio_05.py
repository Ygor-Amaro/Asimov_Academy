#desafio 05

"""
Dado duas listas, printe todos os valores que aparecerem duplicados nas duas listas.
Dado duas listas, printe uma mensagem dizendo se existe algum elemento em comum entre elas ou não.
"""

lista1 = [5, 18, 23, 51, 44.1, 6, 102, -2, -502, -0.5]
lista2 = [7, 51, -2, 0, 3.14, 44.1, 8, -500, 1024]
duplicados = []

# primeira parte do desafio
for elemento in lista1:
    if elemento in lista2:
        duplicados.append(elemento)
print(duplicados)

# segunda parte do desafio
for elemento in lista1:
    if elemento in lista2:
        print("Existe(m) elemento(s) em comum entre as duas listas.")
        break