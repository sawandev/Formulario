import mysql.connector
from pyautogui import alert


def users():
    cnx = mysql.connector.connect(database='agenda', password='Analivia2003!@#', user='root', host='localhost')
    cursor = cnx.cursor()
    
    login = []
    cursor.execute('SELECT login FROM tb_cadastros;')
    r = cursor.fetchone()
    while r is not None:
        login += r
        r = cursor.fetchone()

    cnx.close()
    cursor.close()

    return login

def passwords():
    cnx = mysql.connector.connect(database='agenda', password='Analivia2003!@#', user='root', host='localhost')
    cursor = cnx.cursor()

    senha = []
    cursor.execute('SELECT senha FROM tb_cadastros;')
    r = cursor.fetchone()
    while r is not None:
        senha += r
        r = cursor.fetchone()

    cnx.close()
    cursor.close()

    return senha
 
def record(login, senha):
    cnx = mysql.connector.connect(database='agenda', password='Analivia2003!@#', user='root', host='localhost')
    cursor = cnx.cursor()

    query = f"INSERT INTO tb_cadastros (id, login, senha) VALUES (null, '{login}', '{senha}');"

    cursor.execute(query)
    cnx.commit()

    cnx.close()
    cursor.close()

    return alert('Registrado com sucesso!', 'ALERT!')