import csv
from datetime import datetime

agenda = {}

def gravar():
    nome = input('Nome: ')
    aniversario = input('Aniversario: ')
    email = input('Email: ')
    
    if nome in agenda:
        print("Já existe esse contato.")
        return
    
    telefones = []
    while True:
        tipo = input("Digite o tipo de telefone (celular/fixo/residência/trabalho) ou deixe em branco para finalizar: ")
        if not tipo:
            break
        numero = input("Digite o número de telefone: ")
        telefones.append({"tipo": tipo, "numero": numero})
        
    agenda[nome] = {"Aniversário": aniversario, "Email": email, "Telefones": telefones}   
    print('Adicionado') 
    
    with open('agenda.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Aniversário', 'Email', 'Telefones'])
        for nome, detalhes in agenda.items():
            aniversario = detalhes.get('Aniversário', 'Não especificado')
            email = detalhes['Email']
            telefones = detalhes['Telefones']
            writer.writerow([nome, aniversario, email, telefones])
            
def alterar():
    contato = input('Digite o nome do contato para alterar: ')
    
    while True:
        alterar = input('O que alterar (nome, aniversario, email, telefone): ')

        if alterar == 'nome':
            novo = input('Digite o novo nome: ')
            agenda[novo] = agenda.pop(contato)
            print('Nome alterado!')
            
            
        elif alterar == 'aniversario':
            novo = input('Digite o nova data: ')
            agenda[contato]['Aniversário'] = novo
            print('Data alterado!')    
            
            
        elif alterar == 'email':
            novo = input('Digite o novo email: ')
            agenda[contato]['Email'] = novo
            print('email alterado!') 
            
            
        elif alterar == 'telefone':
            tipo = input('Qual o tipo de telefone que deseja alterar (celular/fixo/residência/trabalho): ')
            novo = input('Digite o novo número: ')

            for telefone in agenda[contato]['Telefones']:
                if telefone['tipo'] == tipo:
                    telefone['numero'] = novo
                    print('alterado!')
                    
            else:
                print(f'Não foi encontrado um telefone do tipo "{tipo}" para o contato "{contato}".')
                         
        else:
            print("Opção inválida.")
            
        
        sair=input('Deseja alterar algo a mais?')
        if sair == 'nao':
            break
        
                
def listar():
    for nome, detalhes in agenda.items():
        aniversario = detalhes.get('Aniversário', 'Não especificado')
        email = detalhes['Email']
        telefones = detalhes['Telefones']
        
        print('\n------------------------------------------')
        print(f"Nome: {nome}")
        print(f"Aniversário: {aniversario}")
        print(f"E-mail: {email}")
        print("Telefones:")
        for telefone in telefones:
            tipo = telefone['tipo']
            numero = telefone['numero']
            print(f"{tipo}:{numero}")

          
def apagar():
    contato = input('Digite o nome do contato para apagar: ')
    
    if contato in agenda:
        del agenda[contato]
        print(f'O contato "{contato}" foi apagado com sucesso!')
    else:
        print(f'O contato "{contato}" não foi encontrado na agenda.')
        
        
def tamanhoPosicoes():
    print(f'Tamanho da agenda: {len(agenda)}')
    print('Posições dos contatos:')
    for i, nome in enumerate(agenda, start=1):
        print(f'{i}. {nome}')
        
def ordenar():
    agendaOrdenada = dict(sorted(agenda.items()))
    agenda = agendaOrdenada
    print("Agenda ordenada em ordem alfabetica.")
                

def ler():
    try:
        with open('agenda.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Ignora o cabeçalho
            for linha in reader:
                nome, aniversario, email, telefones = linha
                agenda[nome] = {"Aniversário": aniversario, "Email": email, "Telefones": eval(telefones)}
        print("Dados da agenda carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo da agenda não encontrado.")
        

def aniversariantes_do_dia():
    hoje = datetime.now().strftime("%d/%m")
    aniversariantes = [nome for nome, detalhes in agenda.items() if detalhes.get('Aniversário') == hoje]
    if aniversariantes:
        print("Aniversariantes do dia:")
        for nome in aniversariantes:
            print(nome)
    else:
        print("Não há aniversariantes hoje.")        

def menu(): 
    while True:
        print('-------------Menu------------')
        print(' 1- Gravar \n 2- Alterar \n 3- Listar \n 4- Ler \n 5- Apagar \n 6- Ordenar \n 7- Ver Tamanho e Posições \n 8- Aniversariantes do Dia\n 0- Sair' )
        escolha = int(input('Selecione: '))
        
        if escolha == 1:
            gravar()    
        elif escolha == 2:
            alterar()   
        elif escolha == 3:
            listar()
        elif escolha == 4:
            ler()
        elif escolha == 5:
            apagar()
        elif escolha == 6:
            ordenar()
        elif escolha == 7:
            tamanhoPosicoes()
        elif escolha == 8:
            aniversariantes_do_dia()
        elif escolha == 0:
            break
        else:           
            print('Opção inválida')


menu()
