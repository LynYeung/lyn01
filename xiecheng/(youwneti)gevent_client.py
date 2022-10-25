import time

import gevent
import sys
from gevent import monkey
monkey.patch_all()
from socket import *

# 创建tcp套接字
s = socket()  # 使用默认参数
server_addr = ("192.168.1.15", 8899) # 设置服务端地址
s.connect(server_addr)

def send(s):
    while 1:
        data = input("msg>>")
        time.sleep(0.5)
        if data == 'quit':
            s.close()
            sys.exit("out of chatroom")
        s.send(('fenxin：'+ data).encode())

def recv(s):
    while 1:
        data = s.recv(1024).decode()
        print(data)



k = gevent.spawn(send, s)
r = gevent.spawn(recv, s)
gevent.joinall([k,r])
