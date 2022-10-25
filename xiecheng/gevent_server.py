"""
基于gevent协程的tcp server
"""
import random

import  gevent
from gevent import monkey
monkey.patch_all()
from socket import *

ADDR = ('0.0.0.0', 8899)
cls = []

def handle(c,cls):
    while 1:
        data = c.recv(1024).decode()
        if not data:
            c.close()
            cls.remove(c)
            break
        print(data)
        for cl in cls:
            cl.send(data.encode())



s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(10)

while 1:
    c, addr = s.accept()
    cls.append(c)
    # print(cls)
    # for i in cls:
    #     print(i)
    print("connect from addr:", addr)
    gevent.spawn(handle,c,cls)

