import math

# Solicita à pessoa usuária que digite dois números inteiros
base = int(input('Digite o primeiro número inteiro (base): '))
expoente = int(input('Digite o segundo número inteiro (expoente): '))

# Calcula a potência do primeiro número elevado ao segundo
resultado = math.pow(base, expoente)

# Exibe o resultado
print(f'O resultado de {base} elevado a {expoente} é: {resultado}')
