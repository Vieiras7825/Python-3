"""
Listas em Python
Tipo list - Mutável
Suporta várias valores de qualquer tipo
Conhecimentos reutilizavéis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#.........+01234
#.........-54321
string = 'ABCDE' # 5 caracteres (len)
lista = [1,2,3, True, 'Sabrina', 1.2, []]
# print(bool(lista)) # falsy
# print(lista, type(lista))
#........0....1......2...........3....4
#.......-5...-4.....-3..........-2...-1
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))