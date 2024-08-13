import random

# Solicita ao usuário o número de participantes
numero_de_participantes = int(input("Por favor, insira o número de participantes do sorteio: "))

# Realiza o sorteio
numero_sorteado = random.randint(1, numero_de_participantes)

# Exibe o número sorteado
print(f"O número sorteado é: {numero_sorteado}")
