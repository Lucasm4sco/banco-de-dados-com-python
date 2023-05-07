def listar_bancos_de_dados(cursor):
    print('Listando databases:')
    cursor.execute('SHOW DATABASES')

    for i, database in enumerate(cursor, start=1):
        print(f'Banco de dados {i}: {database[0]}')