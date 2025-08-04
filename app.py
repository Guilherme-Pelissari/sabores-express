import os

restaurantes = [{'nome':'Burguer King', 'categoria':'Fast Food','ativo':False},
                {'nome':'Garoupa', 'categoria':'Frutos do mar','ativo':True},
                {'nome':'MacDonalds', 'categoria':'Fast Food','ativo':False}]

def exibir_nome_programa():
    print(""" 
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print("1. cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
   exibir_subtitulo('finalizando o app')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('opcao invalida\n')

    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome':nome_restaurante,'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante{nome_restaurante} foi cadastrado com sucesso')

    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante  = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
        
    voltar_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('o restaurante não foi encontrado')    

    voltar_ao_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opçao: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()

