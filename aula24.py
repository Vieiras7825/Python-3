# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# S a b r i n a
# -6-5-4-3-2-1-0

# nome = 'Sabrina'

# print(nome[-2])

#print('á' in nome)

# print('z' in nome)

# print('zero' in nome)

# print(10 * '-')

# print('á' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')    