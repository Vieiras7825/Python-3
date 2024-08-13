"""
Listas em Python
Tipo list - Mutável
Suporta várias valores de qualquer tipo
Conhecimentos reutilizavéis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#........0...1...2...3
lista = [10, 20, 30, 40]
lista.append('Sabrina')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear()
lista.insert(100, 5)
print(lista[4])