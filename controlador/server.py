#!/usr/bin/env python

"""Servidor tcp e udp"""

import socket
import re
import sqlite3
import sys
from threading import Thread

LISTEN_ADDR = 'localhost'
TCP_PORT = 3000
UDP_PORT = 3030
BUFFER_SIZE = 1024


def tcp_listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((LISTEN_ADDR, TCP_PORT))
    s.listen()
    print("Ouvindo em {}:{} TCP".format(LISTEN_ADDR, TCP_PORT))

    try:
        while True:
            conn, address = s.accept()
            Thread(target=tcp_handler, args=(conn, address)).start()
    finally:
        s.close()


def tcp_handler(conn, address):
    print("Conexão TCP de: ", address)
    msg = conn.recv(1024).decode()
    ret = client_handler(msg)
    conn.send(ret.encode())


def udp_listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((LISTEN_ADDR, UDP_PORT))
    print("Ouvindo em {}:{} UDP".format(LISTEN_ADDR, UDP_PORT))

    try:
        while True:
            data, address = s.recvfrom(BUFFER_SIZE)
            Thread(target=udp_handler, args=(data, address)).start()
    finally:
        s.close()


def udp_handler(data, address):
    print("Mensagem UDP de: ", address)
    client_handler(data.decode())


def client_handler(msg):
    op, prod = re.split(r' ', msg)
    with Product() as p:
        if op == 'STOR' or op == 'RETR':
            print("OP: {} PRODUTO: {}".format(op, prod))
            p.save(op, prod)
            return 'ok'
        else:
            return 'Operação invalida'


class Product():
    def __init__(self):
        self.conn = sqlite3.connect('database.db')

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.conn.close()

    def save(self, op, name):
        """Registra uma transação, se o produto existe, sua quantidade é
        alterada, caso contrario o produto é registrado"""

        c = self.conn.cursor()
        print(name)
        if self.exists(name):
            prod_id = self.findId(name)
            c.execute('UPDATE product SET qnt=qnt {} 1 WHERE id=?'
                      .format('+' if op == 'STOR' else '-'),
                      [prod_id])
        else:
            c.execute('INSERT INTO product(name, qnt) VALUES (?, 1)', [name])
            prod_id = self.findId(name)

        c.execute("""INSERT INTO transactions(id_product, date_time, opcode)
        VALUES (?, datetime('now'), ?)""", [prod_id, op])
        c.close()
        self.conn.commit()

    def exists(self, name):
        """ Verifica se existe um produto com o nome igual a `name` """

        c = self.conn.cursor()
        c.execute('SELECT rowid FROM product WHERE name=?',
                  [name])
        d = c.fetchall()
        print("data = {}".format(d))
        return len(d) != 0

    def findId(self, name):
        """ Retorna o id do produto com nome igual a `name` """

        c = self.conn.cursor()
        c.execute('SELECT p.id FROM product p WHERE name=?', [name])
        return c.fetchone()[0]


def main():
    tcp_server = Thread(target=tcp_listener)
    udp_server = Thread(target=udp_listener)

    tcp_server.start()
    udp_server.start()

    try:
        tcp_server.join()
        udp_server.join()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
