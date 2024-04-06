lugares_vagos = [10, 2, 1, 3, 0]

def vender_bilhetes():
    while True:
        sala = int(input("Digite o número da sala (ou 0 para sair): "))
        if sala == 0:
            print("Saindo do programa...")
            break
        elif sala < 1 or sala > len(lugares_vagos):
            print("Sala inválida. Por favor, digite um número de sala válido.")
            continue
        lugares_disponiveis = lugares_vagos[sala - 1]
        if lugares_disponiveis == 0:
            print("Desculpe, não há lugares disponíveis nesta sala.")
        else:
            qtd_solicitada = int(input(f"Quantos lugares você deseja (máximo {lugares_disponiveis}): "))
            if qtd_solicitada <= lugares_disponiveis:
                lugares_vagos[sala - 1] -= qtd_solicitada
                print(f"Venda realizada com sucesso! {qtd_solicitada} lugares vendidos para a sala {sala}.")
            else:
                print("Desculpe, não há lugares suficientes disponíveis nesta sala.")

vender_bilhetes()