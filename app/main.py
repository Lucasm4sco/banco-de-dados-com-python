from criar_banco import criar_banco
from conexao import get_conexao

cnx = get_conexao()
cursor = cnx.cursor()

criar_banco(cursor, 'agenda')
