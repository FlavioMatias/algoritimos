import random

elements = []
size = int(input("Tamanho da lista de elementos: "))

for i in range(size):
    elements.append(random.randint(0, 1000000))


with open('dados.txt', 'w') as file:
    file.write(" ".join(map(str, elements)))

print("Os dados foram gravados no arquivo 'dados.txt'.")
