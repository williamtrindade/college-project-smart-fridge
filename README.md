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


## Funcionamento - Imagens
![dashboard](https://github.com/williamtrindade/Projeto-Smart-Fridge/blob/master/laravel-webapp/img/Screenshot_2019-09-19_23-12-19.png?raw=true)
![products](https://github.com/williamtrindade/Projeto-Smart-Fridge/blob/master/laravel-webapp/img/Screenshot_2019-09-19_23-12-49.png?raw=true)
![transactions](https://github.com/williamtrindade/Projeto-Smart-Fridge/blob/master/laravel-webapp/img/Screenshot_2019-09-19_23-12-00.png?raw=true)
![tcp_udp_client_and_server_storing](https://github.com/williamtrindade/Projeto-Smart-Fridge/blob/master/laravel-webapp/img/Screenshot_2019-09-19_23-12-03.png?raw=true)
