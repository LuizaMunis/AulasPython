lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print("Maior elemento:", max(lista))
print("Menor elemento:", min(lista))

print("Números pares:", [x for x in lista if x % 2 == 0])

print("Número de ocorrências do primeiro elemento:", lista.count(lista[0]))

print("Média dos elementos:", sum(lista) / len(lista))

print("Soma dos elementos de valor negativo:", sum([x for x in lista if x < 0]))