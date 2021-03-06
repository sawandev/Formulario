from PySimpleGUI import PySimpleGUI as sg
from pyautogui import alert

from lib.conexao import *


def subscribe():
    # Tema da janela
    sg.theme('Topanga')

    # Botões e labels
    layout_cad = [
    [sg.Text('Primeiro nome:'), sg.Input(key='novo_usuario', size=(25, 5))],
    [sg.Text('Senha:'), sg.Input(key='nova_senha', password_char='*', size=(32, 5))],
    [sg.Text('Confirmar senha:'), sg.Input(key='conf_nova_senha', password_char='*', size=(24, 5))],
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
            try:
                # Se a as senhas se coincidirem e o novo usuario nao for uma string vazia
                if valores_cad['nova_senha'] == valores_cad['conf_nova_senha'] and valores_cad['novo_usuario'] != '':
                    # Fecha o form e envia os novos dados para o servidor
                    janela_cad.close()                       
                    record(valores_cad['novo_usuario'], valores_cad['nova_senha'])
                
                # Tratamento de erro caso as senhas forem diferentes
                if valores_cad['nova_senha'] != valores_cad['conf_nova_senha']:
                    alert('As senhas não são iguais!', 'ERRO! #009',button='TENTE NOVAMENTE!')
            except:
                alert('Você utilizou caracteres inválidos.', 'ERRO! #007', button='ENTENDI!')
