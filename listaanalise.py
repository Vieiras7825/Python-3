def analisar_desempenho(notas):
    if len(notas) != 4:
        return "Erro: A lista deve conter exatamente 4 notas."
    
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)
    situacao = "aprovado(a)" if media >= 7 else "reprovado(a)"
    
    return f"O(a) estudante obteve uma média de {media:.2f}, com a sua maior nota de {maior_nota} pontos e a menor nota de {menor_nota} pontos e foi {situacao}."

# Testando a função com um exemplo
notas_exemplo = [7.5, 9.0, 6.0, 8.0]
resultado = analisar_desempenho(notas_exemplo)
print(resultado)
