from conexao_database import nova_conexao
from mysql.connector.errors import ProgrammingError

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50),
        tel VARCHAR(40)
    )
"""

tabela_emails = """
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

def criar_tabelas_db_agenda():
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as err:
            print(f'Erro: {err.msg}')