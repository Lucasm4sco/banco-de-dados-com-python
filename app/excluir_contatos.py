from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao


def excluir_contato_pelo_nome(nome):
    sql = 'DELETE FROM contatos WHERE nome = %s'
    args = (nome,)
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
        except ProgrammingError as err:
            print(f'Erro ao excluir contato: {err.msg}')
        else:
            print(f'{cursor.rowcount} registro(s) deletado(s).')