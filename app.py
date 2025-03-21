import os

restaurantes = restaurantes = [ {'nome':'Japan', 'categoria':'Japonesa', 'estado':False}, 
                                {'nome':'Suprema', 'categoria':'Pizza', 'estado':True},
                                {'nome':'Cantina', 'categoria':'Brasileira', 'estado':False}]


def nome_programa():
    '''Exibe o nome do programa no terminal.'''
    print ('𝑴𝒆𝒏𝒖𝑮𝒐 🍴\n')

def exibir_opcoes():
    '''Exibe as opções disponíveis no menu do programa.'''
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurantes')
    print ('3. Alternar estado do restaurante')
    print ('4. Sair\n')

def finalizar_app():
    '''Exibe uma mensagem de despedida e finaliza o programa.'''
    exibir_subtitulo('Obrigado por usar o aplicativo!\n')
    
def voltar_menu():
    '''Aguarda a interação do usuário e retorna ao menu principal.'''
    input('\nAperte qualquer tecla para voltar ao menu... ')
    main()

def opcao_invalida():
    '''Exibe uma mensagem de erro quando o usuário escolhe uma opção inválida e retorna ao menu.'''
    print('Opção inválida!!\n')
    voltar_menu()

def exibir_subtitulo(texto):
    '''Exibe um subtítulo formatado no terminal.
    :param texto: Texto a ser exibido como subtítulo.'''
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def altenar_estado_restaurante():
    '''Alterna o estado (ativo/inativo) de um restaurante cadastrado.
    O usuário deve informar o nome do restaurante. Se encontrado, seu estado será alterado.
    '''
    exibir_subtitulo('Alterando estado restaurante: ')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['estado'] = not restaurante['estado']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['estado'] else f'O restauten {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
        
    voltar_menu()
    

def cadastrar_restaurante():
    '''Permite o cadastro de um novo restaurante e adiciona-o à lista.
    O usuário deve informar o nome e a categoria do restaurante.
    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastar: ')
    categoria = input (f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()
    
    
def lista_restaurantes():
    '''Exibe a lista de restaurantes cadastrados com nome, categoria e estado (ativo/inativo).'''
    exibir_subtitulo('Restaurantes Cadastrados\n')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Estado')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        estado = 'ativado' if restaurante['estado'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {estado}')
    voltar_menu()
    



def escolher_opcao():
    ''' Captura a escolha do usuário e chama a função correspondente.'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                lista_restaurantes()
            case 3:
                altenar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except: opcao_invalida()

    
    
    
    
def main():
    '''Função principal que inicia o programa, exibindo o nome e as opções do menu.'''
    os.system('cls')
    nome_programa()
    exibir_opcoes()
    escolher_opcao()
    
    
if __name__ == '__main__':
    main()
    
    
    
    

   