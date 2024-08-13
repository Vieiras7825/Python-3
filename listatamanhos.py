# Lista fornecida
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# Leitura do tamanho da lista
tamanho = len(lista)

# Leitura do maior e menor valor
maior_valor = max(lista)
menor_valor = min(lista)

# Soma dos valores da lista
soma_valores = sum(lista)

# Soma dos valores pares da lista
soma_pares = sum(valor for valor in lista if valor % 2 == 0)

# Exibindo a mensagem
mensagem = f"A lista possui {tamanho} números em que o maior número é {maior_valor} e o menor número é {menor_valor}. A soma dos valores pares presentes nela é igual a {soma_pares}"
print(mensagem)
