from criar_banco import criar_banco
from conexao import get_conexao
from listar_bancos import listar_bancos_de_dados
from criar_tabelas_db_agenda import criar_tabelas_db_agenda
from deletar_tabela_db_agenda import deletar_tabela_db_agenda
from listar_tabelas import listar_tabelas_database
from alterar_tabela_db_agenda import alterar_tabela_db_agenda
from incluir_contato import incluir_contato, incluir_lista_contatos
from selecionar_contatos import listar_contatos
from filtrando_dados import filtrar_pelo_numero, filtar_pelo_nome
from filtro_por_entrada_de_dados import filtrar_pelo_nome_entrada
from excluir_contatos import excluir_contato_pelo_nome
from atualizar_contato import atualizar_nome_contato

cnx = get_conexao()

if cnx is not False:
    cursor = cnx.cursor()
    criar_banco(cursor, 'agenda')
    listar_bancos_de_dados(cursor)
    cnx.close()

    # Utilizando outro formato de conexão
    criar_tabelas_db_agenda()
    deletar_tabela_db_agenda()

    listar_tabelas_database('agenda')
    alterar_tabela_db_agenda()

    incluir_contato('Lucas', '90765-4321')
    contatos = (
        ('João', '90235-4321'),
        ('Pedro', '93125-4231'),
        ('Maria', '12345-5678'),
        ('Helena', '24521-7743')
    )
    incluir_lista_contatos(contatos)

    listar_contatos(5)

    filtrar_pelo_numero()
    filtar_pelo_nome()
    filtrar_pelo_nome_entrada('Hele')
    
    excluir_contato_pelo_nome('Lucas')
    excluir_contato_pelo_nome('Eduarda')

    atualizar_nome_contato(id=4, nome_atualizado='Ana Julia')
    