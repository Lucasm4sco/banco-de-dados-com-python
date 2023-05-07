from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao

def listar_contatos_paginacao(limite = 10, offset=0 ):
    sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s'
    args = (limite, offset)
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            contatos = cursor.fetchall()
        except ProgrammingError as err:
            print(f'Erro ao selecionar contatos: {err.msg}')
        else:
            print('Listando contatos por paginação: ')

            for contato in contatos:
                print(f'{contato[2]:2d} - {contato[0]:10s} Tefone: {contato[1]}')
