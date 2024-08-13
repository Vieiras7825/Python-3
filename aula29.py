"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

else -> se não houver erro

finally -> sempre executa
"""

numero_str = input('Vou dobrar o número que você digitar: ')
try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except ValueError:
    print('Isso não é um número')

         
# if numero_str.isdigit():
#      numero_float = float(numero_str)
# ....print(f'O dobro de {numero_str} e {numero_float * 2:.2f}')

# else:
#     print('Isso nao e um numero')

