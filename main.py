from pyautogui import alert
import PySimpleGUI as sg

from lib.form_cadastro import *
from lib.conexao import *


def main():
    arq = 'conexao_bd.txt'

    # Se o arquivo conexao_bd.txt não existir
    if not arquivoExiste(arq):
        criarArquivo(arq)

    # Tema da janela
    sg.theme('Topanga')

    # Botões e labels
    layout = [
        [sg.Text('Usuario:'), sg.Input(key='usuario', size=(36, 5))],
        [sg.Text('Senha:'), sg.Input(key='senha', password_char='*', size=(37, 5))],
        [sg.Button('Entrar')],
        [sg.Button('Cadastrar-se')]
    ]

    # Função que verifica a comunicação com o banco de dados
    nome_janela = verifica_cnx()

    janela_login = sg.Window(nome_janela, layout)

    # Lendo os eventos
    while True:
        eventos_login, valores_login = janela_login.read()

        # X fecha a janela
        if eventos_login == sg.WINDOW_CLOSED:
            break

        # Tratamento contra SQL INJECTION, o que não permite o acesso mas quebra a aplicação
        try:
            if eventos_login == 'Entrar':
                # Se os dados conferem
                if login_existente(valores_login['usuario'], valores_login['senha']):
                    alert('''BEM-VINDO \nAO SISTEMA''', f'Bem-vindo {valores_login["usuario"].capitalize()}!', button='Obrigado')

                # Se os dados não conferem
                else:
                    alert('Credenciais incorretas!', 'ERRO!', button='TENTAR NOVAMENTE')
            
            # Ao acionar o evento 'Cadastrar', chama o form de cadastro
            if eventos_login == 'Cadastrar-se':
                subscribe()      
        except:
            alert('Credenciais incorretas! AA', 'ERRO!', button='TENTAR NOVAMENTE')

if __name__ == '__main__':
    main()