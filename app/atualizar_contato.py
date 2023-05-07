from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao


def atualizar_nome_contato(id, nome_atualizado):
    sql = 'UPDATE contatos set nome = %s WHERE id = %s'
    args = (nome_atualizado, id)

    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
        except ProgrammingError as err:
            print(f'Erro ao excluir contato: {err.msg}')
        else:
            print(f'{cursor.rowcount} registro(s) alterados(s).')