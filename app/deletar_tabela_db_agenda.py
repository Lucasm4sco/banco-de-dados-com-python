from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao

def deletar_tabela_db_agenda():
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute('DROP TABLE IF EXISTS emails')
        except ProgrammingError as err:
            print(f'Erro: {err.msg}')

