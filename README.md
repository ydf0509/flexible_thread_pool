# 1. flexible_thread_pool

flexible_thread_pool ，auto expand thread and reduce threads. both support sync and asyncio,fast than concurrent.futures.ThreadpoolExecutor

可扩大和自动缩小的线程池，比 threadpool_executor_shrink_able 实现更简单的线程池，性能超过 concurrent.futures.ThreadpoolExecutor 200%

另一个本人实现的可自动扩大和缩小的线程池： https://github.com/ydf0509/threadpool_executor_shrink_able


说明：
此线程池支持submit 方法，但不支持Future特性，只支持简单粗暴的submit自动并发执行。

## 1.2 flexible_thread_pool 性能说明

在 win11 + r5 4600u 这个很差的cpu 前提下， 单核单进程测试下，100线程池每秒执行3万次 def f(): pass    函数。

## 1.3 重点说明可变线程池和一般线程池区别

例如代码如下:
```python
import time

pool = ThreadpoolExecutor(500)


def f(x):
    time.sleep(10)
    print(x)

for i in  range(10000):
    time.sleep(1)
    time.sleep(100)
    pool.submit(f,i)
```

### 1.3.1 情景1,不需要开很多线程就能应付函数运行
```
假设每隔100秒 submit一个任务到pool中,愚蠢的 ThreadpoolExecutor 线程池会一直扩大到500线程,
但是 FlexibleThreadPool 即使你设置最大线程为500,也只会开1个线程,因为你每隔100秒才会提交下一个运行,
而函数只要10秒就能运行完,那需要开500线程做什么?

FlexibleThreadPool 会用最智能的线程数量来应付任务,自适应调节,既不会多开线程浪费,
也不会少开线程导致单位时间内运行函数次数变少.
```

### 1.3.2 情景2,流量高峰过后线程池自动缩小

假设你 9:00 到10:00, 每隔0.00001秒submit一个任务到pool, 10:00后每隔 2秒submit一个任务到pool

```
愚蠢的线程池,任何时候一直保持线程数量是500

智能的自适应线程池 FlexibleThreadPool,因为9:00-10:00 是流量高峰,而f函数需要10秒才能运行完,
所以9:00-10:00 会火力全开,开到500线程.
10:00后每隔 2秒submit一个任务到pool,而f需要耗时10秒,FlexibleThreadPool会自动减少到5个线程,
刚好使得线程消费和发布速度100%匹配.
FlexibleThreadPool 时时刻刻在自适应调整线程数量
```


### 1.3.3 FlexibleThreadPool 是无视函数耗时多少,自适应调节线程数量.

```
FlexibleThreadPool 并不能自动读取f函数的逻辑,开启天眼知道f函数是耗时10秒,而是真正的自动调整,
它无需用户自己提前分析预估一个函数需要耗时多久,来评估计算需要指定一个合理的线程池大小,完全不需要.
```


# 2. 安装
pip install flexible_thread_pool


# 3 用法

FlexibleThreadPool 能够支持同步函数和asyncio异步函数的并发执行。

```python
import asyncio
import time
from flexible_thread_pool import FlexibleThreadPool


def testf(x):
    time.sleep(10)
    if x % 10000 == 0:
        print(x)


async def aiotestf(x):
    await asyncio.sleep(1)
    if x % 10 == 0:
        print(x)
    return x * 2


pool = FlexibleThreadPool(100)
# pool = ThreadPoolExecutor(100)

for i in range(20000):
    # time.sleep(2)
    pool.submit(aiotestf, i)
```



