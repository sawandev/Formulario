from lib.interface import *
from lib.conexao import *


def main():
    from pyautogui import alert

    # Tema da janela
    sg.theme('Black')

    # Botões e labels
    layout = [
        [sg.Text('Usuario'), sg.Input(key='usuario', size=(30, 3))],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(31, 3))],
        [sg.Button('Entrar')],
        [sg.Button('Cadastrar')]
    ]

    janela_login = sg.Window('Entrar', layout)

    # Lendo os eventos
    while True:
        eventos_login, valores_login = janela_login.read()

        # X fecha a janela
        if eventos_login == sg.WINDOW_CLOSED:
            break

        if eventos_login == 'Entrar':
            # Confere o login e senha no BD e atualiza as listas
            login = users()
            senha = passwords()

            # Se os dados conferem
            if valores_login['usuario'] in login and valores_login['senha'] in senha:
                alert('BEM-VINDO AO SISTEMA', f'Bem-vindo {valores_login["usuario"]}', button='Obrigado!')

            # Se os dados não conferem
            else:
                alert('Credenciais incorretas!', 'ERRO!', button='TENTAR NOVAMENTE')
        
        if eventos_login == 'Cadastrar':
            subscribe()

if __name__ == '__main__':
    main()