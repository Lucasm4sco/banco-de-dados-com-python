from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao

def incluir_grupos():
    sql = 'INSERT INTO grupos(descricao) VALUES(%s)'
    args = (
        ('Casa',),
        ('Trabalho',)
    )
    with nova_conexao('agenda') as conexao:
        try:
            print('Adicionando dados tabela grupos...')
            cursor = conexao.cursor()
            cursor.executemany(sql, args)
            conexao.commit()
        except ProgrammingError as err:
            print(f'Erro ao adicionar dados: {err.msg}')
        else:
            print(f'Foram incluídos {cursor.rowcount} registro(s).')