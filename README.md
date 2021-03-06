# Projeto-Smart-Fridge

Projeto feito para a disciplina de Redes de computadores 'A', com foco
em implementar um cliente e servidor TCP e UDP com uma ideia criativa.

# Ideia
Uma geladeira inteligente que identifica o produto e registra suas
transações (inserção e remoção de dentro da geladeira)

## Cliente (python)
Um controlador com uma câmera dentro da geladeira, ele identifica o
produto inserido/retirado na geladeira e envia para o servidor
registrando o acontecimento.

## Servidor TCP/UDP (python)
Registra as transações de um produto em um banco sqlite.

## Aplicação web (php)
A visualização das transações é feita na web por uma aplicação
laravel.

# Banco
Foi usado sqlite.

## Schema
### Products
 - id         : SERIAL
 - name       : VARCHAR(30)
 - amount     : INT
 - created_at : datetime
 - updated_at : datetime

### Transactions
 - id         : SERIAL
 - product_id : INT
 - date_time  : datetime
 - opcode     : CHAR(4) valores:[RETR, STOR]
 - created_at : datetime
 - updated_at : datetime

## Funcionamento
![dashboard](https://media.giphy.com/media/kyRTVZrwxHFZSsJw8v/giphy.gif)
