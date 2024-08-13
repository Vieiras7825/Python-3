import os

lista = []

while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar: ")

    if opcao == "i":
        os.system("clear" if os.name == "posix" else "cls")
        valor = input("Valor: ")
        lista.append(valor)
    elif opcao == "a":
        os.system("clear" if os.name == "posix" else "cls")
        try:
            indice_str = input("Escolha o índice para apagar: ")
            indice = int(indice_str)
            del lista[indice]
        except (ValueError, IndexError):
            print("Índice inválido. Tente novamente.")
    elif opcao == "l":
        os.system("clear" if os.name == "posix" else "cls")
        if len(lista) == 0:
            print("Nada para listar")
        else:
            for i, valor in enumerate(lista):
                print(i, valor)
    else:
        print("Por favor, escolha i, a ou l.")
