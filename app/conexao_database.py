from mysql.connector import connect
from contextlib import contextmanager

@contextmanager
def nova_conexao(database):
    parametros = dict(
        host='localhost',
        user='root',
        password='root',
        database=database
    )
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if conexao and conexao.is_connected():
            conexao.close()