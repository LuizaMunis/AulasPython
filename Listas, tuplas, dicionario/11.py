
eu = {
    'nome': 'luiza',
    'sobrenome': 'munis',
    'idade': 22,
    'cidade': 'uruaçu'
}

maria = {
    'nome': 'maria',
    'sobrenome': 'silva',
    'idade': 25,
    'cidade': 'goiania'
}

joao = {
    'nome': 'joao',
    'sobrenome': 'pereira',
    'idade': 30,
    'cidade': 'brasilia'
}

pessoa = [eu, maria, joao]

for pessoas in pessoa:
    print(f"Nome: {pessoas['nome']}")
    print(f"Sobrenome: {pessoas['sobrenome']}")
    print(f"Idade: {pessoas['idade']}")
    print(f"Cidade: {pessoas['cidade']}")
    print("\n")