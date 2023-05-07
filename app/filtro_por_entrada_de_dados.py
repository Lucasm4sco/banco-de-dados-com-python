from mysql.connector.errors import ProgrammingError
from conexao_database import nova_conexao

def filtrar_pelo_nome_entrada(nome):
    sql = "SELECT * FROM contatos WHERE nome LIKE %s"
    args= (f'%{nome}%',)

    with nova_conexao('agenda') as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)

            print(f'Listando nomes que contenham {nome}: ')

            for valores in cursor:
                print(valores[0])

        except ProgrammingError as err:
            print(f'Erro ao filtrar contato: {err.msg}')