import random

def gerar_token():
    # Gera um número par aleatório entre 1000 e 9998
    return random.randrange(1000, 9999, 2)

def main():
    # Solicita o nome do usuário
    nome = input("Por favor, insira seu nome: ")
    
    # Gera o token
    token = gerar_token()
    
    # Exibe a mensagem com o nome do usuário e o token gerado
    print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")

# Executa o programa
if __name__ == "__main__":
    main()
