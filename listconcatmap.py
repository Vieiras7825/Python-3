# Listas fornecidas
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

# Função para formatar o nome completo
def formatar_nome_completo(nome, sobrenome):
    return f"Nome completo: {nome.capitalize()} {sobrenome.capitalize()}"

# Utilizando map para combinar as listas e formatar os nomes
nomes_completos = list(map(formatar_nome_completo, nomes, sobrenomes))

# Exibindo os nomes completos
for nome_completo in nomes_completos:
    print(nome_completo)
