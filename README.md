# 1. flexible_thread_pool

flexible_thread_pool ，auto expand thread and reduce threads. both support sync and asyncio,fast than concurrent.futures.ThreadpoolExecutor

可扩大和自动缩小的线程池，比 threadpool_executor_shrink_able 实现更简单的线程池，性能超过 concurrent.futures.ThreadpoolExecutor 200%

另一个本人实现的可自动扩大和缩小的线程池： https://github.com/ydf0509/threadpool_executor_shrink_able


说明：
此线程池支持submit 方法，但不支持Future特性，只支持简单粗暴的submit自动并发执行。

## 1.2 flexible_thread_pool 性能说明

在 win11 + r5 4600u 这个很差的cpu 前提下， 单核单进程测试下，100线程池每秒执行3万次 def f(): pass    函数。


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



