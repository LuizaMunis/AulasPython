
def comparar_listas(lista_inicial, lista_alterada):
    conjunto_inicial = set(lista_inicial)
    conjunto_alterado = set(lista_alterada)
    nao_mudaram = conjunto_inicial.intersection(conjunto_alterado)

    novos_elementos = conjunto_alterado - conjunto_inicial
    removidos = conjunto_inicial - conjunto_alterado

    print("Elementos que não mudaram:")
    print(nao_mudaram)
    print("\nNovos elementos:")
    print(novos_elementos)
    print("\nElementos que foram removidos:")
    print(removidos)

lista_inicial = [1, 2, 3, 4, 5]
lista_alterada = [2, 3, 5, 6, 7]

print("Comparação entre as listas:")
comparar_listas(lista_inicial, lista_alterada)