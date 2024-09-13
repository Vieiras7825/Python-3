
#Manipulando chaves e valores em dicionários
# Dicionário de pessoa
pessoa = {}

# Adicionando valores ao dicionário
chave = 'nome'

pessoa['nome'] = 'Luiz Otávio'
pessoa[chave] = 'Maria'

# Imprime o valor da chave 'nome'
print(pessoa[chave])

# Atualizando a chave 'nome' novamente
pessoa[chave] = 'Maria'

# Tentando remover uma chave que não existe
# Aqui, podemos verificar se 'sobrenome' existe antes de tentar remover
if pessoa.get('sobrenome') is not None:
    del pessoa['sobrenome']
else:
    print("'sobrenome' não existe para remover")

# Imprime o valor da chave 'nome'
print(pessoa['nome'])

# Verifica se 'sobrenome' existe e tenta acessar seu valor
sobrenome = pessoa.get('sobrenome')
if sobrenome is None:
    print("'sobrenome' não existe")
else:
    print(sobrenome)

# Exemplo de checagem de existência de 'sobrenome'
if pessoa.get('sobrenome') is None:
    print('sobrenome NÃO EXISTE')
else:
    print('sobrenome EXISTE')




    
