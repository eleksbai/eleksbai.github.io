import time

from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@192.168.146.129//', backend='redis://192.168.146.129')


@app.task
def add(x, y):
    # 占时间12秒
    for i in range(123456):
        a = 999 ** 999
        del a
    return x + y


def test_run():
    r1 = add.delay(10, 1)
    r2 = add.delay(10, 2)
    i = 1
    while 1:
        print('第%s秒' % i, r1.result, r2.result)
        if r1.result and r2.result:
            break
        time.sleep(1)
        i += 1

