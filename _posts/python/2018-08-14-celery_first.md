---
layout: default
title: celery_first 官网基础入门教程
date:   2018-08-14 16:16:01 
categories: python
---
# celery_first 最小实验
## 概述
celery 将工作进行分解为：

函数，调用函数，结果容器，函数结果

1. 初始化函数准备工作
2. 调用函数立即返回一个结果容器
3. 函数接收任务开始工作，抛出函数结果
4. 函数结果去填充到结果容器

## 工作者

工作者示例代码
tasks.py
~~~python
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@192.168.146.129//', backend='redis://192.168.146.129')


@app.task
def add(x, y):
    # 占时间12秒
    for i in range(123456):
        a = 999 ** 999
        del a
    return x + y
~~~

工作者流程
1. 准备工作，监听消息队列，获取任务安排
2. 取到任务马上工作，工作完成写入到后端。（工作者是否并发待测试） 

启动工作者
celery -A your_app_name worker --pool=solo -l info
windows下使用报错解决方案
celery -A your_app_name worker --pool=solo -l info

## 安排工作者进行工作

调用工作者执行任务流程
1. 导入工作者的任务方法
2. 执行任务方法
3. 立即返回一个异步结果，包含该执行任务的id
4. 异步结果包含任务结果，初始状态为空，工作者完成工作后自动取得任务结果

**内存假想**

立即返回的结果指向一块内存区间，内存区间有一部分初始状态。
当工作者任务结束会把结果数据写到该内存区间



调用工作者示例代码
tasks.py（续）
~~~python
import time
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
~~~

调用工作者方法
1. pycharm 运行 tasks.py文件，勾选 Run with Python console
2. test_run()
