def criar_banco(cursor, nome):
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {nome}')

