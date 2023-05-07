import time
from mysql.connector import connect


def get_conexao():
    print('Iniciando tentativa de conexão...')
    start_time = time.time()

    while True:
        try:
            cnx = connect(user='root', password='root', host='localhost')
            print('Conexão realizada com sucesso!')
            return cnx
        except:
            if time.time() - start_time > 60:
                print("Não foi possível realizar a conexão!")
                return False

            continue

