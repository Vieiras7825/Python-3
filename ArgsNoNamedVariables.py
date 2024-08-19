"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
#Lembrete de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#    return x + y

def soma(*args):
    print(args)
    total = 0
    for numero in args:
        print('Total', total)
        total = total + numero
        print('Total', total)
    return total    
    
soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)  

soma_1_2_3 = soma(4, 5, 6)
# print(soma_1_2_3)  

outra_soma = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(outra_soma)

print(sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
# print(*numeros)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
outra_soma = soma(numeros)
print(outra_soma)
