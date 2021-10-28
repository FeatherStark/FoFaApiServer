# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 18:47
# @File    : Client.py
import socket


def tcp_server_link():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '127.0.0.1' # 设置服务器的ip,如127.0.0.1
    server_port = 7654 # 设置服务器绑定的端口 如7654
    tcp_client_socket.connect((server_ip, server_port)) 
    return tcp_client_socket


def tcp_client_send(tcp_client_socket):
    send_data = input("FoFaQuery:")
    tcp_client_socket.send(send_data.encode('utf-8'))
    # tcp_client_socket.close()  # 关闭tcp客户端


def tcp_client_recv(tcp_client_socket):
    recv_data = tcp_client_socket.recv(2048) 
    print(recv_data.decode('utf-8'))  


def main():
    tcp_client_socket = tcp_server_link()
    print("Socket链接已经建立。")
    tcp_client_send(tcp_client_socket)
    tcp_client_recv(tcp_client_socket)
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
