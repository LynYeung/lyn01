from time import time
from threading import *
from multiprocessing import *

def count():
    c = 0
    x = 0
    y = 0
    while c < 7000000:
        x += 3
        y += 2
        c += 1

def write():
    f = open("ceshi","w")
    for i in range(3000000):
        f.write("hello, python!%d\n"%i)
    f.close()

def read():
    f = open("ceshi","r")
    f.read()
    f.close()

def io():
    write()
    read()

class CS():
    def __init__(self,act):
        self.act = act

    def single(self):
        self.act()

    def multiproces4(self):
        prcs = []
        for i in range(4):
            p = Process(target=self.act)
            prcs .append(p)
            p.start()
        for p in prcs:
            p.join()

    def multithred4(self):
        thrds = []
        for i in range(4):
            t = Thread(target=self.act)
            thrds.append(t)
            t.start()
        for t in thrds:
            t.join()

def tst(s):
    t1 = time()
    s()
    t2 = time()
    print(t2 - t1)

act_io = io
cs_io = CS(act_io)
act_cnt = count
cs_cnt = CS(act_cnt)

io_sig = cs_io.single
io_multprcs = cs_io.multiproces4
io_multthd = cs_io.multithred4

cnt_sig = cs_cnt.single
cnt_multprcs = cs_cnt.multiproces4
cnt_multthd= cs_cnt.multithred4

print('io_sig time:', end=" ")
tst(io_sig)
print("io_multprcs time:", end=" ")
tst(io_multprcs)
print("io_multthd time:", end=" ")
tst(io_multthd)
print('cnt_sig time:', end=" ")
tst(cnt_sig)
print("cnt_multprcs time:", end=" ")
tst(cnt_multprcs)
print("cnt_multthd time:", end=" ")
tst(cnt_multthd)