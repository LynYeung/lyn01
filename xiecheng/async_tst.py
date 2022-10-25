import asyncio


async def func1():
    print("start func1...")
    await asyncio.sleep(2)
    print("end func1")

async def func2():
    print("start func2...")
    await asyncio.sleep(4)
    print("end func2")

async def func3():
    print("start func3...")
    await asyncio.sleep(2.5)
    print("end func3")



cor1 = func1()
cor2 = func2()
cor3 = func3()
cor4 = func1()

task = [asyncio.ensure_future(cor1),
        asyncio.ensure_future(cor2),
        asyncio.ensure_future(cor3),
        asyncio.ensure_future(cor4)
        ]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
