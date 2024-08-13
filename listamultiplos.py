def filtrar_multiplos_de_tres(lista):
    multiplos_de_tres = [numero for numero in lista if numero % 3 == 0]
    return multiplos_de_tres

# Lista fornecida
lista_original = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# Utilizando a função e salvando o resultado na variável mult_3
mult_3 = filtrar_multiplos_de_tres(lista_original)

# Exibindo a nova lista com múltiplos de 3
print(mult_3)
