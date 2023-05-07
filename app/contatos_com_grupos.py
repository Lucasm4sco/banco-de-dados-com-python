from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao

sql = """
    SELECT 
        grupos.descricao AS grupo,
        contatos.nome AS contato
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, contato
"""

def listar_contatos_com_grupos():
    with nova_conexao('agenda') as conexao:
        try:
            print('Listando junção de tabelas:')
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql)
            contatos = cursor.fetchall()
        except ProgrammingError as err:
            print(f'Erro ao selecionar junção: {err.msg}')
        else:
            for contato in contatos:
                print(f'{contato["grupo"]}: {contato["contato"]}')