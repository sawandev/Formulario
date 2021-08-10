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