import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Cria a figura e os eixos
fig, ax = plt.subplots()

# Adiciona retângulo sólido
ax.add_patch(patches.Rectangle((1, 1), 2, 2, fill=False, edgecolor="black"))

# Adiciona retângulo tracejado
ax.add_patch(patches.Rectangle((0.5, 0.5), 3, 3, fill=False, edgecolor="black", linestyle="dashed"))

# Ajusta os limites dos eixos para garantir que os retângulos estejam visíveis
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

# Remove os eixos para maior semelhança com a imagem fornecida
plt.axis("off")

# Exibe o gráfico
plt.show()



