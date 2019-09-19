#!/usr/bin/env python3

import socket
import argparse

HOST = 'localhost'


def enviar_msg_tcp(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, 3000))
    s.send(msg.encode())
    print(s.recv(4096))


def enviar_msg_udp(msg):
    s = socket.socket(socket.AF_INET,
                      socket.SOCK_DGRAM)
    s.sendto(msg.encode(), (HOST, 3030))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('modo', choices=('tcp', 'udp'),
                        default='tcp', nargs='?')
    parser.add_argument('msg', type=str)
    args = parser.parse_args()

    if args.modo == 'tcp':
        enviar_msg_tcp(args.msg)
    else:
        enviar_msg_udp(args.msg)


if __name__ == '__main__':
    main()
