from criar_banco import criar_banco
from conexao import get_conexao
from listar_bancos import listar_bancos_de_dados

cnx = get_conexao()
cursor = cnx.cursor()

criar_banco(cursor, 'agenda')
listar_bancos_de_dados(cursor)