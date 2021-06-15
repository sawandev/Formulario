from lib.conexao import *
from PySimpleGUI import PySimpleGUI as sg


def subscribe():
    from pyautogui import alert

    # Tema da janela
    sg.theme('Black')

    # Botões e labels
    layout_cad = [
    [sg.Text('Primeiro nome'), sg.Input(key='novo_usuario', size=(20, 3))],
    [sg.Text('Senha'), sg.Input(key='nova_senha', password_char='*', size=(27, 3))],
    [sg.Text('Confirmar senha'), sg.Input(key='conf_nova_senha', password_char='*', size=(19, 3))],
    [sg.Button('Cadastrar-me')]
    ]

    janela_cad = sg.Window('Cadastro', layout_cad)

    # Lendo os eventos
    while True:
        eventos_cad, valores_cad = janela_cad.read()

        # X fecha a janela        
        if eventos_cad == sg.WINDOW_CLOSED:
            break
        
        # Se clicar no botão para enviar os novos dados
        if eventos_cad == 'Cadastrar-me':
            # Se a as senhas se coincidirem e o novo usuario nao for uma string vazia
            if valores_cad['nova_senha'] == valores_cad['conf_nova_senha'] and valores_cad['novo_usuario'] != '':
                # Envia os novos dados para o servidor                        
                record(valores_cad['novo_usuario'], valores_cad['nova_senha'])

            # Tratamento de erro caso as senhas forem diferentes
            if valores_cad['nova_senha'] != valores_cad['conf_nova_senha']:
                alert('ERRO! As senhas não são iguais!', 'TENTE NOVAMENTE!')