
def ler_listas(listasTxt):
    with open('RevisaoPorva1\listas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        n = int(linhas[0])
        listas = [linha.split()[1:] for linha in linhas[1:]]
    return listas


def contar_ocorrencias(listas):
    ocorrencias = {}
    for lista in listas:
        for elemento in lista:
            if elemento in ocorrencias:
                ocorrencias[elemento] += 1
            else:
                ocorrencias[elemento] = 1
    return ocorrencias

def elementos_unicos(listas):
    elementos_unicos = []
    ocorrencias = contar_ocorrencias(listas)
    for elemento, count in ocorrencias.items():
        if count == 1:
            elementos_unicos.append(elemento)
    return elementos_unicos


def elementos_ultima_lista(listas):
    return set(listas[-1]) - set(listas[0])


def saida(elementos_unicos, ocorrencias, elementos_ultima_lista):
    with open('listasSaida.txt', 'w') as arquivo_saida:
        arquivo_saida.write(f"Elementos que aparecem uma unica vez: {elementos_unicos}\n\n")
        arquivo_saida.write(f"Repeticoes: {ocorrencias}\n\n")
        arquivo_saida.write(f"Elementos presentes na ultima lista mas nao na primeira: {elementos_ultima_lista}\n")


listas = ler_listas('RevisaoPorva1\listas.txt')
unicos = elementos_unicos(listas)
ocorrencias = contar_ocorrencias(listas)
elementos_ultima = elementos_ultima_lista(listas)
saida(unicos, ocorrencias, elementos_ultima)



