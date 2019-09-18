#!/usr/bin/env python

"""Servidor tcp e udp"""

import socket
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
            address
            Thread(target=tcp_handler, args=(conn, address)).start()
    finally:
        s.close()


def tcp_handler(conn, address):
    print("Conexão TCP de: ", address)
    data = conn.recv(1024)
    print("Mesage: ", data)
    conn.send(b"OK")
    conn.close()


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
    print("Message: ", data.decode("utf-8"))


def main():
    tcp_server = Thread(target=tcp_listener)
    udp_server = Thread(target=udp_listener)

    tcp_server.start()
    udp_server.start()

    try:
        tcp_server.join()
        udp_server.join()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
