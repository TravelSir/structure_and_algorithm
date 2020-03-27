import functools
import time


# 打印执行时间帽子
def func_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.time() * 1000
        res = func(*args, **kwargs)
        end = time.time() * 1000
        print(f'执行了: {end - begin}毫秒')
        return res
    return wrapper
