lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

set1 = set(lista1)
set2 = set(lista2)

print("Valores comuns:", set1.intersection(set2))
print("Valores apenas na primeira lista:", set1.difference(set2))
print("Valores apenas na segunda lista:", set2.difference(set1))
print("Elementos não repetidos:", set1.symmetric_difference(set2))
print("Primeira lista sem elementos repetidos na segunda:", set1 - set2)
