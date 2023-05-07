from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao

sql = 'ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

def alterar_tabela_db_agenda():
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
        except ProgrammingError as e:
            print(f'Erro ao alterar tabela: {e.msg}')