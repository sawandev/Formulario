from lib.conexao import *
from PySimpleGUI import PySimpleGUI as sg
from pyautogui import alert


def login():
    #layout
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuario'), sg.Input(key='usuario', size=(20, 1))],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
        [sg.Button('Entrar')],
        [sg.Button('Cadastrar')]
    ]

    # Janela
    janela_login = sg.Window('Tela de login', layout)

    # Ler os eventos
    while True:
        eventos_login, valores_login = janela_login.read()
        if eventos_login == sg.WINDOW_CLOSED:
            break

        if eventos_login == 'Entrar':
            # Banco de dados
            login = users()
            senha = passwords()

            if valores_login['usuario'] in login and valores_login['senha'] in senha:
                alert('O client ira se inciar em breve...', 'Bem-vindo ao sistema!')
            else:
                alert('Login ou senha incorretos!', 'ALERT!')
        
        if eventos_login == 'Cadastrar':
            subscribe()


def subscribe():
    #layout
    sg.theme('Reddit')
    layout_cad = [
    [sg.Text('Primeiro nome'), sg.Input(key='novo_usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='nova_senha', size=(20,1))],
    [sg.Text('Confirmar senha'), sg.Input(key='conf_nova_senha', size=(20,1))],
    [sg.Button('Cadastrar-me')]
    ]

    # Janela
    janela_cad = sg.Window('Tela de cadastro', layout_cad)

    # Ler eventos
    while True:
        eventos_cad, valores_cad = janela_cad.read()
                
        if eventos_cad == sg.WINDOW_CLOSED:
            break

        if eventos_cad == 'Cadastrar-me':
            if valores_cad['nova_senha'] == valores_cad['conf_nova_senha'] and valores_cad['novo_usuario'] != '':
                # Recollect the database users
                login = users()
                senha = passwords()
                        
                record(valores_cad['novo_usuario'], valores_cad['nova_senha'])

        else:
            alert('As senhas estao diferentes!')