from conexao_database import nova_conexao
from mysql.connector.errors import ProgrammingError
from random import choice


def associar_grupo_contato(contatos):
    
    atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

    with nova_conexao('agenda') as conexao:
        try:
            print('Associando contatos com grupos...')
            cursor = conexao.cursor()
            grupos = ('Casa', 'Trabalho')
            grupo_id = grupos.index(choice(grupos)) + 1

            for valores in  contatos:
                cursor.execute(atualizar_contato, (grupo_id, valores[0]))
                conexao.commit()

        except ProgrammingError as err:
            print(f'Erro ao associar dados: {err.msg}')
        else:
            print(f'Contatos foram associados com sucesso!')