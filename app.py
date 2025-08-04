import os  # Módulo para interagir com o sistema operacional, usado para limpar a tela

# Lista inicial de restaurantes com nome, categoria e status (ativo/desativado)
restaurantes = [
    {'nome': 'Burguer King', 'categoria': 'Fast Food', 'ativo': False},
    {'nome': 'Garoupa', 'categoria': 'Frutos do mar', 'ativo': True},
    {'nome': 'MacDonalds', 'categoria': 'Fast Food', 'ativo': False}
]

def exibir_nome_programa():
    # Imprime o nome estilizado do programa com arte ASCII
    '''
    Exibe o nome estilizado do programa na tela
    Inputs:
    - Nenhum
    Outputs:
    - Impressão do nome do programa no terminal
    '''
    print(""" 
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    # Imprime o menu principal com as opções disponíveis
    '''
    Exibe as opções disponíveis no menu principal
    Inputs:
    - Nenhum
    Outputs:
    - Impressão das opções no terminal
    '''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    # Encerra o programa com um subtítulo
    '''
    Finaliza o aplicativo
    Inputs:
    - Nenhum
    Outputs:
    - Mensagem de encerramento
    '''
    exibir_subtitulo('finalizando o app')

def voltar_ao_menu():
    # Pausa o programa e volta para o menu principal após uma entrada do usuário
    '''
    Solicita que o usuário pressione uma tecla para voltar ao menu principal
    Inputs:
    - Nenhum
    Outputs:
    - Retorno ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    # Exibe mensagem de erro ao receber uma opção inválida
    '''
    Trata opções inválidas digitadas pelo usuário
    Inputs:
    - Nenhum
    Outputs:
    - Mensagem de erro e retorno ao menu principal
    '''
    print('opcao invalida\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    # Limpa a tela e imprime um subtítulo formatado com asteriscos
    '''
    Exibe um subtítulo com decoração
    Inputs:
    - texto (str): Texto a ser exibido como subtítulo
    Outputs:
    - Impressão do subtítulo formatado no terminal
    '''
    os.system('cls')  # Limpa o terminal no Windows
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    # Recebe dados do novo restaurante e adiciona à lista
    '''
    Essa função é responsável por cadastrar um novo restaurante
    Inputs: 
    - Nome do restaurante
    - Categoria
    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    exibir_subtitulo('cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso')

    voltar_ao_menu()

def listar_restaurantes():
    # Exibe todos os restaurantes com nome, categoria e status
    '''
    Lista todos os restaurantes cadastrados
    Inputs:
    - Nenhum
    Outputs:
    - Impressão da lista de restaurantes formatada
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')

    voltar_ao_menu()

def alternar_estado_restaurante():
    # Procura restaurante pelo nome e alterna o estado ativo/desativado
    '''
    Alterna o estado (ativo/desativado) de um restaurante
    Inputs:
    - Nome do restaurante a ser alterado
    Outputs:
    - Altera o estado do restaurante se encontrado
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']  # Alterna o valor booleano
            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso'
                if restaurante['ativo'] else
                f'o restaurante {nome_restaurante} foi desativado com sucesso'
            )
            print(mensagem)
    if not restaurante_encontrado:
        print('o restaurante não foi encontrado')

    voltar_ao_menu()

def escolher_opcoes():
    # Lê a opção digitada e chama a função correspondente
    '''
    Captura e processa a opção escolhida pelo usuário
    Inputs:
    - Entrada do usuário via teclado
    Outputs:
    - Executa a função correspondente à opção escolhida
    '''
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
        # Captura erro de entrada inválida (como letras ao invés de números)
        opcao_invalida()

def main():
    # Ponto de entrada principal do programa
    '''
    Função principal que inicializa o programa
    Inputs:
    - Nenhum
    Outputs:
    - Executa a sequência inicial do programa
    '''
    os.system('cls')  # Limpa a tela no Windows
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()

# Garante que o main só será executado se o script for executado diretamente
if __name__ == '__main__':
    main()
