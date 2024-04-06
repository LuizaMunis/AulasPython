sandwich_orders = ['sanduíche de atum', 'sanduíche de frango', 'sanduíche vegetariano', 'sanduíche de presunto e queijo']
finished_sandwiches = []


for pedido in sandwich_orders:
    print(f"Preparando o seu {pedido}.")

    finished_sandwiches.append(pedido)

print("\nSanduíches preparados:")
for sanduiche in finished_sandwiches:
    print(sanduiche)
