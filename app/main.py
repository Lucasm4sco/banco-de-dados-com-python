from criar_banco import criar_banco
from conexao import get_conexao
from listar_bancos import listar_bancos_de_dados
from criar_tabelas_db_agenda import criar_tabelas_db_agenda
from deletar_tabela_db_agenda import deletar_tabela_db_agenda
from listar_tabelas import listar_tabelas_database
from alterar_tabela_db_agenda import alterar_tabela_db_agenda
from incluir_contato import incluir_contato

cnx = get_conexao()

if cnx is not False:
    cursor = cnx.cursor()
    criar_banco(cursor, 'agenda')
    listar_bancos_de_dados(cursor)
    cnx.close()

    criar_tabelas_db_agenda()
    deletar_tabela_db_agenda()

    listar_tabelas_database('agenda')
    alterar_tabela_db_agenda()

    incluir_contato('Lucas', '90765-4321')
    