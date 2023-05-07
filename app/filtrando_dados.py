from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao

def filtrar_pelo_numero():
    sql = "SELECT * FROM contatos WHERE tel = '90765-4321'"
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)

            print('Listando valores filtrados pelo número: ')
            for valores in cursor:
                print(valores)

        except ProgrammingError as err:
            print(f'Erro ao filtrar contato: {err.msg}')


def filtar_pelo_nome():
    sql = "SELECT * FROM contatos WHERE nome LIKE '%a%'"
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)

            print('Listando nomes que contenham letra A: ')
            for valores in cursor:
                print(valores[0])

        except ProgrammingError as err:
            print(f'Erro ao filtrar contato: {err.msg}')
        
            