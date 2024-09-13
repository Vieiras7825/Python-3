# Definição das perguntas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# Função do quiz
def quiz(perguntas):
    score = 0
    for pergunta in perguntas:
        print(pergunta['Pergunta'])
        for i, opcao in enumerate(pergunta['Opções']):
            print(f"{i + 1}. {opcao}")
        
        while True:
            try:
                resposta = int(input("Escolha a opção correta (1-4): "))
                if 1 <= resposta <= 4:
                    break
                else:
                    print("Por favor, escolha um número entre 1 e 4.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        
        if pergunta['Opções'][resposta - 1] == pergunta['Resposta']:
            score += 1
            print("Correto!\n")
        else:
            print("Errado!\n")
    
    print(f"Você acertou {score} de {len(perguntas)} perguntas.")

# Executando o quiz
quiz(perguntas)


