pets = [
    {'nome': 'Rex', 'tipo': 'cachorro', 'dono': 'João'},
    {'nome': 'Mia', 'tipo': 'gato', 'dono': 'Maria'},
    {'nome': 'Piu-Piu', 'tipo': 'pássaro', 'dono': 'Pedro'},
    {'nome': 'Nemo', 'tipo': 'peixe', 'dono': 'Ana'}
]

for pet in pets:
    print(f"Nome: {pet['nome']}")
    print(f"Tipo: {pet['tipo']}")
    print(f"Dono: {pet['dono']}")
    print("\n")
