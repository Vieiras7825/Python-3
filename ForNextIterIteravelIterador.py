"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez next -> me entregue o próximo valor
next -> me entregue seu iterador 
"""
# for letra in texto
#texto = iter('Luiz') #iterável

#iteratador = iter(texto) #iterator

#while True:
#    try:
#        letra = next(iteratador)
#        print(letra)
#    except StopIteration:
#        break
for letra in texto:
    print(letra)