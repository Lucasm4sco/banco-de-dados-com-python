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


tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(30)
    )
"""

alterar_tabela_contato_1 = """
    ALTER TABLE contatos ADD grupo_id INT
"""

alterar_tabela_contato_2 = """
    ALTER TABLE contatos ADD FOREIGN KEY(grupo_id)
    REFERENCES grupos(id)
"""

def criar_tabela_grupo_db_agenda():
    with nova_conexao('agenda') as conexao:
        try:
            print('Criando tabela grupos e relacionando com contatos...')
            cursor = conexao.cursor()
            cursor.execute(tabela_grupo)
            cursor.execute(alterar_tabela_contato_1)
            cursor.execute(alterar_tabela_contato_2)
        except ProgrammingError as err:
            print(f'Erro ao relacionar: {err.msg}')