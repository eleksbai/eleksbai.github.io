import time
def t(n):
    t1 = time.clock()
    for i in range(n):
        a = 999**999
        del a
    print('耗时', time.clock()-t1)


def long_time():
    """预计耗时：12.994573367345314"""
    t1 = time.clock()

    for i in range(123456):
        a = 999**999
        del a

    print('耗时', time.clock() - t1)

long_time()