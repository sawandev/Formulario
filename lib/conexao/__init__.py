import mysql.connector
from pyautogui import alert
import PySimpleGUI as sg


def form_cria_arquivo_bd():
    # Tema da janela
    sg.theme('Dark')

    # Botões e labels
    layout = [
        [sg.Text('Database:'), sg.Input(key='database', size=(32, 5))],
        [sg.Text('Password:'), sg.Input(key='password', password_char='*', size=(32, 5))],
        [sg.Text('User:'), sg.Input(key='user', size=(36, 5))],
        [sg.Text('Host:'), sg.Input(key='host', size=(36, 5))],
        [sg.Button('Conectar-se')],
    ]

    nome_janela = "Conexão - Banco de dados"
    janela_conexao = sg.Window(nome_janela, layout)

    # Lendo os eventos
    while True:
        eventos_bd, valores_bd = janela_conexao.read()

        # X fecha a janela
        if eventos_bd == sg.WINDOW_CLOSED:
            break

        # Se encontra o banco de dados
        if eventos_bd == 'Conectar-se':
            if encontra_bd(
                valores_bd['database'], 
                valores_bd['password'], 
                valores_bd['user'], 
                valores_bd['host']):

                # Insere os dados do banco de dados no arquivo .txt
                cadastrar(
                    'conexao_bd.txt', 
                    valores_bd['database'], 
                    valores_bd['password'], 
                    valores_bd['user'], 
                    valores_bd['host']
                )

                # Fecha o form
                janela_conexao.close()

                # Informa que encontrou o banco de dados
                alert('Banco de dados encontrado e salvo com sucesso!', 'SUCESSO!')

            else:
                alert('Banco de dados NÃO encontrado, por favor, confira os campos.', 'ERRO! #011', button='TENTE NOVAMENTE')

# Encontra o banco de dados
def encontra_bd(database, password, user, host):
    try:
        cnx = mysql.connector.connect(
            database=f"{database}", 
            password=f"{password}", 
            user=f"{user}", 
            host=f"{host}"
        )

        if cnx.is_connected():
            return True
        else:
            return False

    except:
        return False      

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        alert('Houve um erro na criação do aquivo!', 'ERRO! #013', button='TENTE NOVAMENTE')
    else:
        form_cria_arquivo_bd()

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        alert('ERRO: Ao ler o arquivo!', 'ERRO! #015', button='TENTE NOVAMENTE')
    else:
        for argumento in a:
            dado = argumento.split(';')
        return dado
    finally:
        a.close()

def cadastrar(arq, database, password, user, host):
    try:
        a = open(arq, 'at')
    except:
        alert('Houve um erro ao abrir o arquivo!', 'ERRO! #017', button='TENTE NOVAMENTE')
    else:
        try:
            a.write(f'{database};{password};{user};{host};')
        except:
            alert('Houve um erro ao escrever os dados.', 'ERRO! #019', button='TENTE NOVAMENTE')
        finally:
            a.close()

# Confere se existe o usuário no banco
def login_existente(login, senha):
    itens_conexao = lerArquivo('conexao_bd.txt')  

    cnx = mysql.connector.connect(database=itens_conexao[0], password=itens_conexao[1], user=itens_conexao[2], host=itens_conexao[3])
    cursor = cnx.cursor()

    # Chama a STORED PROCEDURE que devolve TRUE para usuário encontrado e FALSE para não encontrado
    query = f"""CALL
                    sp_busca_cadastros
                            ("{login}",
                             "{senha}");
    """

    cursor.execute(query)

    r = cursor.fetchone()

    try:
        existe = list(r)
        if login == existe[0] and senha == existe[1]:
            cnx.close()
            cursor.close()
            return True
    except:
        return False

# Registra um novno usuário no banco
def record(login, senha):
    itens_conexao = lerArquivo('conexao_bd.txt')  
      
    cnx = mysql.connector.connect(database=itens_conexao[0], password=itens_conexao[1], user=itens_conexao[2], host=itens_conexao[3])
    cursor = cnx.cursor()

    query = f"""CALL 
                    sp_cadastrar
                            ("{login}",
                             "{senha}");
    """

    cursor.execute(query)
    cnx.commit()

    cnx.close()
    cursor.close()

    return alert('Registrado com sucesso!', 'SUCESSO!')
