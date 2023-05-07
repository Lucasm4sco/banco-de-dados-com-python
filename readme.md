# Banco de dados com python

## Sobre

Atividade realizada para aprendizado na manipulação de um banco de dados com a lib **mysql-connector-python** do python, tbm utilizei do docker para firmalizar conceitos no uso de containers.

## Executar com o docker

Para executar use os comandos no terminal:

- `docker compose -p db-com-python up` -> Irá contruir e inicializar as imagens (irá aparecer alguns logs das mudanças no db).
- `docker exec -it mysql bash` -> Irá abrir um terminal interativo para o container rodando o mysql.
- `mysql -u root -p` -> Vai pedir uma password, digite **root** e você será levado ao MySQL monitor, onde vai poder verificar as mudanças realizadas no banco de dados.