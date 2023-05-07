from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao

def listar_contatos(limite = 15):
    sql = 'SELECT * FROM contatos LIMIT ' + str(limite)
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            contatos = cursor.fetchall()
        except ProgrammingError as err:
            print(f'Erro ao selecionar contatos: {err.msg}')
        else:
            print('Listando contatos em agenda: ')

            for contato in contatos:
                print(f'{contato[2]:2d} - {contato[0]:10s} Tefone: {contato[1]}')
