import gevent
from gevent import monkey
gevent.monkey.patch_all()
import time

def func1(a,b):

    print(f"start func1...{a}--{b}")
    time.sleep(2)
    print(input())
    print("end func1")

def func2():
    i = 0.5
    while i < 1:
        i += 0.3
        time.sleep(i)
        print(f"run func2{i}...")


def func3():
    i = 0.5
    while i < 1:
        i += 0.2
        time.sleep(i)
        print(f"run func3{i}...")

def func4():
    i = 0.5
    while i < 2:
        i += 0.5
        time.sleep(i)
        print(f"run func4{i}...")


t1 = time.time()
#f1 = gevent.spawn(func1, 1, 2)
while 1:
    print(input())
    print("end func1")
f2 = gevent.spawn(func2)
f3 = gevent.spawn(func3)
f4 = gevent.spawn(func4)
gevent.joinall([f2,f3,f4])


