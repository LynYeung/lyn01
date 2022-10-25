from greenlet import greenlet

def func1():
    print("start func1...")
    gr2.switch()
    print("end func1")


def func2():
    print("start func2...")
    gr3.switch()
    print("end func2")


def func3():
    print("start func3...")
    gr1.switch()
    print("end func3")

gr1 = greenlet(func1)
gr2 = greenlet(func2)
gr3 = greenlet(func3)

gr2.switch()
gr1.switch()
gr3.switch()