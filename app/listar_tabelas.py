from conexao_database import nova_conexao

def listar_tabelas_database(database):
    with nova_conexao(database) as conexao:
        cursor = conexao.cursor()
        cursor.execute('SHOW TABLES')
        print('Listando tabelas do database: ' + database)

        for i, table in enumerate(cursor):
            print(f'Tabela {i}: {table[0]}')