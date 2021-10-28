# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 18:40
# @File    : ServerSocket.py
import socket
import requests
import base64
import time


def FofaServerQuery(QueryType):
    QBASE64 = base64.b64encode(QueryType.encode('utf-8'))
    Femail = "" #这里填写fofa会员邮箱
    Fkey = "" # 这里填写fofa会员的key
    url = f"https://fofa.so/api/v1/search/all?email={email}&key={Fkey}&qbase64={str(QBASE64,encoding='utf-8')}&size=200&full=True"
    resp = requests.get(url=url)
    return resp.content.decode("utf-8")


def RunLog(Query, addr):
    with open("log.txt", "a+", encoding='utf-8') as log:
        log.writelines("查询地址："+str(addr[0])+":"+str(addr[1])+"\n")
        log.writelines("查询时间："+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+"\n")
        log.writelines("查询语法："+Query+"\n\n\n")


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('', 7654))  # 填写绑定服务器接收socket端口
    tcp_server_socket.listen(128)  
    while True:
        try:
            print('正在等待链接客户端。。。')
            new_client, client_addr = tcp_server_socket.accept() 
            print('客户端已连接')
            while True:
                recv_data = new_client.recv(1024)  
                print(new_client.getpeername())
                print("当前时间："+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                print(f'客户端查询语句：{recv_data.decode("utf-8")}')
                RunLog(recv_data.decode("utf-8"), new_client.getpeername())
                option_or_massg = FofaServerQuery(recv_data.decode("utf-8"))
                new_client.send(option_or_massg.encode('utf-8'))  
                if recv_data:
                    new_client.close()
                    break
            print("\n\n上一个链接已关闭，等待下一个链接中：")
        except ConnectionError:
            continue
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
