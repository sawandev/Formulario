import mysql.connector


def login_existente(login, senha):
    from pyautogui import alert 
    
    cnx = mysql.connector.connect(database='agenda', password='Analivia2003!@#', user='root', host='localhost')
    cursor = cnx.cursor()

    query = f"""SELECT 
                    login, 
                    senha 
                FROM 
                    tb_cadastros 
                WHERE 
                    login = '{login}' and 
                    senha = '{senha}';"""

    cursor.execute(query)

    r = cursor.fetchone()

    try:
        existe = list(r)
        if login == existe[0] and senha == existe[1]:
            return True
    except:
        return False

def record(login, senha):
    from pyautogui import alert

    cnx = mysql.connector.connect(database='agenda', password='Analivia2003!@#', user='root', host='localhost')
    cursor = cnx.cursor()

    query = f"""INSERT INTO 
                    tb_cadastros (id, 
                                login, 
                                senha) 
                VALUES          
                                ( null, 
                                '{login}', 
                                '{senha}' );"""

    cursor.execute(query)
    cnx.commit()

    cnx.close()
    cursor.close()

    return alert('Registrado com sucesso!', 'SUCESSO!')

def verifica_cnx():
    nome_janela = 'SAWAN - Sistema Online'

    try:
        cnx = mysql.connector.connect(database='agenda', password='Analivia2003!@#', user='root', host='localhost')
    except:
        nome_janela = 'SAWAN - Sistema Offline'
    
    return nome_janela

"""
Necessário criar uma única função responsável pela comunicação com o BD, 
por que não adianta verificar a conexão em todas as função os parâmetros de
cnx são utilizados.
IDEIA: Adição de uma função que se caso seja a primeira entrada do usuário,
que seja pedido os parâmetros do banco de dados para ele, e então, que esses
dados sejam gravados em um arquivo .txt e buscado por cada função quando 
necessário. Assim dava para incrementar algum tipo de criptografia nesse
novo arquivo, podendo esconder os parâmetros do banco de dados e permite 
a conexão em databases com outros nomes (porem com os mesmo campos).
"""