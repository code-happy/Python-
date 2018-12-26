# -*- coding:utf-8 -*-
import socket
def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.连接服务器
    # tcp_socket.connect("",7890)
    server_ip = input("请输入IP")
    server_port = int(input("请输入端口"))
    server_addr = (server_ip,server_port)
    tcp_socket.connect(server_addr)
    # 发送数据
    send_mess = input("请输入需要发送的数据")
    tcp_socket.send(send_mess.encode("utf_8"))
if __name__ == '__main__':
    main()