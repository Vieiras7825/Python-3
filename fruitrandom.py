import random

# Lista de frutas disponíveis
frutas = ["maçã", "banana", "uva", "pêra", "manga", "coco", "melancia", "mamão", "laranja", "abacaxi", "kiwi", "ameixa"]

# Seleciona 3 frutas aleatoriamente da lista
salada_surpresa = random.sample(frutas, 3)

# Exibe as frutas selecionadas
print(f"As frutas selecionadas para a 'Salada de Frutas Surpresa' são: {salada_surpresa}")
