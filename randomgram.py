import math

# Solicita ao usuário o raio da área circular
raio = float(input("Por favor, insira o raio da área circular em metros: "))

# Calcula a área do círculo
area = math.pi * math.pow(raio, 2)

# Calcula o custo da grama
preco_por_metro_quadrado = 25.00
custo = area * preco_por_metro_quadrado

# Exibe o valor a ser pago
print(f"O valor total a pagar pela grama é de R$ {custo:.2f}")
