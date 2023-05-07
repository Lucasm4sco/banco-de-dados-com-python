from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao

sql = 'INSERT INTO contatos(nome, tel) VALUES(%s, %s)'

def incluir_contato(nome, telefone):
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, (nome, telefone))
            conexao.commit()
        except ProgrammingError as err:
            print(f'Erro ao adicionar dados: {err.msg}')
        else:
            print('1 Registo incluído, ID:', cursor.lastrowid)


def incluir_lista_contatos(lista):
    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.executemany(sql, lista)
            conexao.commit()
        except ProgrammingError as err:
            print(f'Erro ao adicionar dados: {err.msg}')
        else:
            print(f'Foram incluídos {cursor.rowcount} registro(s).')