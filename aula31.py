"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade    
"""

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Nao faca algo') 

if passou_no_if is None:
    print('Nao passou no if')

if passou_no_if is None:
    print('Passou no if')     