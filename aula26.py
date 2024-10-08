# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere) (><)^(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a __repr__ __str__ __abs__
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10+,.1f}')
print('O hexadecimal de 1500 e {1500:08X}')
print(f'{variavel!r}')
